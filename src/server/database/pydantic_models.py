from pydantic import BaseModel

BaseModelModify = BaseModel


class CourierCompany(BaseModel):
    id: int
    name: str
    contact_email: str
    contact_phone: str


class Courier(BaseModel):
    id: int
    name: str
    contact_email: str
    contact_phone: str
    company_id: int


class Package(BaseModel):
    id: int
    tracking_number: str
    weight: float
    delivery_status: str
    sender_address_id: int
    recipient_address_id: int
    courier_id: int


class Address(BaseModel):
    id: int
    street: str
    city: str
    state: str
    postal_code: str


class Invoice(BaseModel):
    id: int
    package_id: int
    total_amount: float
    payment_status: str


class Employee(BaseModel):
    id: int
    name: str
    position: str
    contact_email: str
    contact_phone: str
    login: str
    password: str


class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address_id: int
    login: str
    password: str


class UserRole(BaseModel):
    id: int
    user_id: int
    role_name: str


class Transaction(BaseModel):
    id: int
    invoice_id: int
    amount: float
    transaction_date: str


class PaymentMethod(BaseModel):
    id: int
    name: str
