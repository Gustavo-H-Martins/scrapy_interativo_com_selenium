import code
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class productSchema(BaseModel):
    code: int = Field(...)
    barcode: str = Field(...)
    status: str = Field(...)
    imported_t: datetime = Field(...)
    url: str = Field(...)
    product_name: str = Field(...)
    quantity: str = Field(...)
    categories: str = Field(...)
    packaging: str = Field(...)
    brands: str = Field(...)
    image_url: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "code": 3661112502850,
                "barcode": "3661112502850(EAN / EAN-13)",
                "status": "imported",
                "imported_t": "2020-02-07T16:00:00Z",
                "url": "https://world.openfoodfacts.org/product/3661112502850",
                "product_name": "Jambon de Paris cuit à l'étouffée",
                "quantity": "240 g",
                "categories": "Meats, Prepared meats, Hams, White hams",
                "packaging": "Film en plastique, Film en plastique",
                "brands": "Tradilège, Marque Repère",
                "image_url": "https://static.openfoodfacts.org/images/products/366/111/250/2850/front_fr.3.400.jpg"
            }          
        }


class UpdateProductModel(BaseModel):
    code: Optional[int]
    barcode: Optional[str]
    status: Optional[str]
    imported_t: Optional[datetime]
    url: Optional[str]
    product_name: Optional[str]
    quantity: Optional[str]
    categories: Optional[str]
    packaging: Optional[str]
    brands: Optional[str]
    image_url: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "code": 3661112502850,
                "barcode": "3661112502850(EAN / EAN-13)",
                "status": "imported",
                "imported_t": "2022-02-07T16:00:00Z",
                "url": "https://world.openfoodfacts.org/product/3661112502850",
                "product_name": "Jambon de Paris cuit à l'étouffée",
                "quantity": "250 g",
                "categories": "vegans, Prepared vegetables, Hams, White hams",
                "packaging": "Film en plastique, Film en plastique",
                "brands": "Tradilège, Marque Repère",
                "image_url": "https://static.openfoodfacts.org/images/products/366/111/250/2850/front_fr.3.400.jpg"
            } 
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}