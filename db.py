from pydantic import BaseModel
import datetime

class Reserva(BaseModel):
    habitacion_id:int
    usuario_id:str
    fecha_inicio: datetime.date
    fecha_fin: datetime.date

reservas={
    1:Reserva(habitacion_id=1,usuario_id=1,fecha_inicio='2020-12-24',fecha_fin='2021-01-14'),
    2:Reserva(habitacion_id=2,usuario_id=2,fecha_inicio='2020-12-24',fecha_fin='2021-01-15')

}



def obtener_lista_reservas():
    lista_reservas=[]
    for reserva in reservas:
        lista_reservas.append(reservas[reserva])
        
    return lista_reservas
    
#if (reservas[reserva][fecha_inicio]>fecha_inicial) and (reservas[reserva][fecha_final]<fecha_final) :
            

