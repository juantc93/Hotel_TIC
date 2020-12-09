from fastapi import FastAPI,HTTPException
import db

app=FastAPI()

@app.get("/reservas")
async def obtener_ocupacion():
    return db.obtener_lista_reservas()