from fastapi import FastAPI, Request

from modelo import modelo
app = FastAPI()

@app.post("/")

async def root(request: Request):
    json = modelo(await request.json())
    if 2 in json:
        return {"message": 'Sentimento Neutro'}
    elif 1 in json:
       return {"message": 'Sentimento Positivo'}
    else:
       return {"message": 'Sentimento Negativo'}