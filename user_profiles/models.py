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
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mechanic_detail'



class ServiceHistory(models.Model):
    mech_id = models.IntegerField()
    owner_id = models.IntegerField()
    catagory = models.CharField(max_length=30)
    rating = models.IntegerField(default=5)
    comments = models.TextField(default=None)
    car = models.CharField(max_length=30, default=None, db_column='car_info')
    vehicle = models.IntegerField(default=0)
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

