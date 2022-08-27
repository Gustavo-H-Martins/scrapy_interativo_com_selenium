from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

# Adicionando as rotas para complementar as operações do banco de dados no arquivo de banco de dados.
from app.server.database import (
    add_product,
    delete_product,
    retrieve_product,
    retrieve_product,
    update_product,
)
from app.server.models.product import (
    ErrorResponseModel,
    ResponseModel,
    productSchema,
    UpdateproductModel,
)

router = APIRouter()