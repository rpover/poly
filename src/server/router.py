from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import RouterManager

routers = (
    RouterManager(
        database_model=database_models.CourierCompany,
        pydantic_model=pydantic_models.CourierCompany,
        prefix='/courier_company',
        tags=['CourierCompany']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Courier,
        pydantic_model=pydantic_models.Courier,
        prefix='/courier',
        tags=['Courier']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Package,
        pydantic_model=pydantic_models.Package,
        prefix='/package',
        tags=['Package']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Address,
        pydantic_model=pydantic_models.Address,
        prefix='/address',
        tags=['Address']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Invoice,
        pydantic_model=pydantic_models.Invoice,
        prefix='/invoice',
        tags=['Invoice']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Employee,
        pydantic_model=pydantic_models.Employee,
        prefix='/employee',
        tags=['Employee']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Customer,
        pydantic_model=pydantic_models.Customer,
        prefix='/customer',
        tags=['Customer']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.UserRole,
        pydantic_model=pydantic_models.UserRole,
        prefix='/user_role',
        tags=['UserRole']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Transaction,
        pydantic_model=pydantic_models.Transaction,
        prefix='/transaction',
        tags=['Transaction']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.PaymentMethod,
        pydantic_model=pydantic_models.PaymentMethod,
        prefix='/payment_method',
        tags=['PaymentMethod']
    ).fastapi_router,
)