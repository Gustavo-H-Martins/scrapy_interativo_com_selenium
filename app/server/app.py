from fastapi import FastAPI

from app.server.routes.product import router as productRouter

#Home
app = FastAPI()
# Link Root: https://localhost:8000/docs#/
#Lik indice https://localhost:8000/

# Chamando a rota de produtos
app.include_router(productRouter, tags=["produtc"], prefix="/product")
# criando uma rota base
# Link Root: https://localhost:8000/docs#/
#Lik indice https://localhost:8000/
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Isso é um teste para ver a conexão, diga olá!"}


