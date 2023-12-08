import peewee

db = peewee.SqliteDatabase('database.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class CourierCompany(BaseModel):
    name = peewee.CharField(null=False, default='')
    contact_email = peewee.CharField(null=False, default='')
    contact_phone = peewee.CharField(null=False, default='')


class Courier(BaseModel):
    name = peewee.CharField(null=False, default='')
    contact_email = peewee.CharField(null=False, default='')
    contact_phone = peewee.CharField(null=False, default='')
    company_id = peewee.ForeignKeyField(CourierCompany, backref='couriers')


class Address(BaseModel):
    street = peewee.CharField(null=False, default='')
    city = peewee.CharField(null=False, default='')
    state = peewee.CharField(null=False, default='')
    postal_code = peewee.CharField(null=False, default='')


class Package(BaseModel):
    tracking_number = peewee.CharField(null=False, default='')
    weight = peewee.FloatField(null=False, default=0)
    delivery_status = peewee.CharField(null=False, default='')
    sender_address_id = peewee.ForeignKeyField(Address, backref='sender_packages')
    recipient_address_id = peewee.ForeignKeyField(Address, backref='recipient_packages')
    courier_id = peewee.ForeignKeyField(Courier, backref='packages')


class Invoice(BaseModel):
    package_id = peewee.ForeignKeyField(Package, backref='invoice')
    total_amount = peewee.FloatField(null=False, default=0)
    payment_status = peewee.CharField(null=False, default='')


class Employee(BaseModel):
    name = peewee.CharField(null=False, default='')
    position = peewee.CharField(null=False, default='')
    contact_email = peewee.CharField(null=False, default='')
    contact_phone = peewee.CharField(null=False, default='')
    login = peewee.CharField(null=False, default='')
    password = peewee.CharField(null=False, default='')


class Customer(BaseModel):
    name = peewee.CharField(null=False, default='')
    email = peewee.CharField(null=False, default='')
    phone = peewee.CharField(null=False, default='')
    address_id = peewee.ForeignKeyField(Address, backref='customers')
    login = peewee.CharField(null=False, default='')
    password = peewee.CharField(null=False, default='')


class UserRole(BaseModel):
    user_id = peewee.ForeignKeyField(Customer, backref='user_roles')
    role_name = peewee.CharField(null=False, default='')


class Transaction(BaseModel):
    invoice_id = peewee.ForeignKeyField(Invoice, backref='transactions')
    amount = peewee.FloatField(null=False, default=0)
    transaction_date = peewee.DateTimeField()


class PaymentMethod(BaseModel):
    name = peewee.CharField(null=False, default='')


db.create_tables([
    CourierCompany,
    Courier,
    Address,
    Package,
    Invoice,
    Employee,
    Customer,
    UserRole,
    Transaction,
    PaymentMethod
])
