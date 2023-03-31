from fastapi import FastAPI
from pydantic import BaseModel
from http import HTTPStatus


app = FastAPI()

@app.get("/")
def olaMundo():
    return "Ola"



class Carro(BaseModel):
    nome: str
    price: float
    tax: float  = None


@app.post("/carros/",status_code = HTTPStatus.CREATED)
def createCar(carro : Carro):
    return carro


