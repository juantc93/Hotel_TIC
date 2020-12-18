from fastapi import FastAPI,HTTPException
import db
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
origins=[
    "http//localhost.tiangolo.com","https://localhost.tiangolo.com",
    "http//localhost","http://localhost:8080","https://prueba-frontend-hotel-tic.herokuapp.com",
]

app.add_middleware(
    CORSMiddleware,allow_origins=origins,
    allow_credentials=True, allow_methods=["*"],allow_headers=["*"],
)
@app.get("/reservas/ocupacion")
async def obtener_ocupacion():
    return db.obtener_lista_reservas()


@app.post("/reservas/crear")
async def crear_reserva(reserva: db.Reserva):
    reserva_exitosa = db.crear_reserva(reserva)
    if reserva_exitosa:
        return{"Mensaje": "Reservación creada con éxito"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo realziar la reservación")