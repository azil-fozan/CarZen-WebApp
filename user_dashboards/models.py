from datetime import timedelta
from carzen.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from user_dashboards.constants import PHONE_NUMBER_VALIDATION_MESSAGE

class Receipt(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    created_by = models.ForeignKey('carzen.User', db_column='created_by', on_delete=CASCADE)
    customer = models.ForeignKey('Customer', db_column='customer', on_delete=CASCADE)
    status = models.CharField(max_length=30, db_column='status', default='inactive')
    paid_amount = models.IntegerField(db_column='paid_amount', default=0)
    active_date = models.DateTimeField(db_column='active_date', null=True, default=timezone.now)
    created_date = models.DateTimeField(db_column='created_date', default=timezone.now)
    expiry_date = models.DateTimeField(db_column='expiry_date', default=timezone.now() + timedelta(days=10))
    purchase_order_number = models.IntegerField(db_column='purchase_order_number', default=0)
    payment_term = models.CharField(max_length=30, db_column='payment_term', null=True)

    class Meta:
        db_table = 'receipt'

class Customer(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=40, db_column='name')
    address = models.CharField(max_length=40, db_column='address')
    reference = models.CharField(max_length=80, db_column='reference')
    created_date = models.DateTimeField(db_column='created_date', default=timezone.now)
    phone_number = models.CharField(db_column='phone_number',
                                    max_length=13,
                                    validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                               message=PHONE_NUMBER_VALIDATION_MESSAGE)],
                                    default=None)
    created_by = models.ForeignKey('carzen.User', db_column='created_by', on_delete=CASCADE, default=None)

    class Meta:
        db_table = 'customer'

class Address(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    address_string = models.CharField(max_length=100, db_column='address_string')
    created_date = models.DateTimeField(db_column='created_date', default=timezone.now)

    class Meta:
        db_table = 'address'

class CustomerAddresses(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    customer = models.ForeignKey('Customer', db_column='customer', on_delete=CASCADE, null=True)
    address = models.ForeignKey('Address', db_column='address', on_delete=CASCADE)

    class Meta:
        db_table = 'customer_addresses'

class Product(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(db_column='name', max_length=100)
    price = models.IntegerField(db_column='price', default=0)
    unit = models.CharField(db_column='unit', max_length=30, default='kilograms')
    quantity = models.IntegerField(db_column='quantity', default=0)
    discount = models.IntegerField(db_column='discount', null=True, default=0)
    created_date = models.DateTimeField(db_column='created_date', default=timezone.now)
    created_by = models.ForeignKey('carzen.User', db_column='created_by', on_delete=CASCADE)

    class Meta:
        db_table = 'product'

class Bill(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    receipt_id = models.ForeignKey('Receipt', db_column='receipt_id', on_delete=CASCADE)
    product_id = models.ForeignKey('Product', db_column='product_id', on_delete=CASCADE)
    quantity = models.IntegerField(db_column='quantity', default=0)
    created_date = models.DateTimeField(db_column='created_date', default=timezone.now)
    added_by = models.ForeignKey('carzen.User', db_column='created_by', on_delete=CASCADE)

    class Meta:
        db_table = 'bill'

