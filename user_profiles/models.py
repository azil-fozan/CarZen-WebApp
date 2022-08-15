from django.db.models import CASCADE

from django.db import models
import datetime

def get_utc_time():
    return datetime.datetime.utcnow()

class Bill(models.Model):
    quantity = models.IntegerField()
    created_date = models.DateTimeField()
    # created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by')
    # product = models.ForeignKey('Product', models.DO_NOTHING)
    # receipt = models.ForeignKey('Receipt', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill'


class MechanicDetail(models.Model):
    expertise = models.CharField(max_length=30)
    updated_on = models.DateTimeField(blank=True, null=True, default=get_utc_time)
    user = models.ForeignKey('BI.User', on_delete=CASCADE, null=True, db_column='user_id')

    class Meta:
        managed = False
        db_table = 'mechanic_detail'


class ServiceHistory(models.Model):
    mech_id = models.IntegerField()
    owner_id = models.IntegerField()
    catagory = models.CharField(max_length=30)
    rating = models.IntegerField(default=0)
    rating_owner = models.IntegerField(default=0)
    comments = models.TextField(default=None)
    comments_owner = models.TextField(default=None)
    service_info = models.TextField(default=None)
    car = models.CharField(max_length=30, default=None, db_column='car_info')
    status = models.CharField(max_length=30, default='Open')
    status_owner = models.CharField(max_length=30, default='Open')
    vehicle = models.IntegerField(default=0)
    appointment_datetime = models.DateTimeField(default=None)
    appointed = models.BooleanField(default=False)
    expected_bill = models.IntegerField(default=0)
    total_bill = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=get_utc_time)

    class Meta:
        managed = False
        db_table = 'service_history'


class Receipt(models.Model):
    status = models.CharField(max_length=30)
    paid_amount = models.IntegerField()
    active_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    purchase_order_number = models.IntegerField()
    payment_term = models.CharField(max_length=30, blank=True, null=True)
    # created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by')
    # customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer')

    class Meta:
        managed = False
        db_table = 'receipt'

