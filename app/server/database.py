import code
from bson.objectid import ObjectId
from itertools import product
import motor.motorasyncio


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.products

product_collection = database.get_collection("products_collection")
# Função Auxiliar


def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "code": product["code"],
        "barcode": product["barcode"],
        "status": product["status"],
        "imported_t": product["imported_t"],
        "product_name": product["product_name"],
        "quantity": product["quantity"],
        "categories": product["categories"],
        "packaging": product["packaging"],
        "brands": product["brands"],
        "image_url": product["image_url"]
    }
# Recuperar todos os produtos presentes no banco de dados
async def retrieve_product():
    products = []
    async for product in product_collection.find():
        products.append(product_helper(product))
    return products

# Adicionar um novo produto ao banco de dados
async def add_product(product_data: dict) -> dict:
    product = await product_collection.insert_one(product_data)
    new_product = await product_collection.find_one({"_id": product.inserted_id})
    return product_helper(new_product)

# Recuperar um produto com um Código correspondente
async def retrieve_product(code: str) -> dict:
    product = await product_collection.find_one({"code": ObjectId(code)})
    if product:
        return product_helper(product)


# Atualizar um produto com um Código correspondente
async def update_product(cpde: str, data: dict):
    # Retorna "false" se um corpo de solicitação vazio for enviado.
    if len(data) < 1:
        return False
    product = await product_collection.find_one({"code": ObjectId(code)})
    if product:
        updated_product = await product_collection.update_one(
            {"code": ObjectId(code)}, {"$set": data}
        )
        if updated_product:
            return True
        return False


# Excluir um Produto do banco de dados
async def delete_product(code: str):
    product = await product_collection.find_one({"code": ObjectId(code)})
    if product:
        await product_collection.delete_one({"code": ObjectId(code)})
        return True
