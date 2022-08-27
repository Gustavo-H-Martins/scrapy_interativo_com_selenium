from pymongo import ReadPreference
import uvicorn
import asyncio
import motor.motor_asyncio

# ponto de entrada para executar o aplicativo
if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
# adicionando as informações de conexão do banco de dados

MONGO_DETAILS = "mongodb+srv://admin:admin@offgustavo.rrosmdt.mongodb.net/?retryWrites=true&w=majority"
#"mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.products

student_collection = database.get_collection("products_collection")    