from carzen import settings
from user_dashboards.models import Bill
from tempfile import NamedTemporaryFile
import boto3


def get_receipt_product_data(receipt_id=0, data=None):
    if not data:
        data = Bill.objects.filter(receipt_id__id=receipt_id)

    response_data = []
    for row in data:
        temp_dict = {}
        temp_dict['id'] = row.id
        temp_dict['product_name'] = row.product_id.name
        temp_dict['unit'] = row.product_id.unit
        temp_dict['price'] = row.product_id.price
        temp_dict['discount'] = row.product_id.discount
        temp_dict['quantity'] = row.quantity
        temp_dict['total'] = round(
            (temp_dict['quantity'] * temp_dict['price']) * (1 - (temp_dict['discount'] / 100)), 2)
        response_data.append(temp_dict)
    return response_data


def download_file(bucket, key):
    s3 = boto3.client("s3", aws_access_key_id=settings.AWS_S3_ACCESS_KEY,
                          aws_secret_access_key=settings.AWS_S3_SECRET_KEY)
    s3_data = s3.get_object(Bucket= bucket, Key = key)
    contents = s3_data['Body'].read()  # your Excel's essence, pretty much a stream
    return contents
