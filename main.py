import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

# http://127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}
# http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaotest():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudante/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

@app.delete("estudante/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0