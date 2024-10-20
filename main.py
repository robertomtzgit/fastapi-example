from fastapi import FastAPI
from models import Nombre
from fastapi import HTTPException

app = FastAPI()

# Lista inicial de nombres (puede reemplazarse por datos dinámicos más tarde)
nombres = [
    Nombre(id=1, nombre="Juan", apellido="Pérez", edad=30),
    Nombre(id=2, nombre="María", apellido="Gómez", edad=25),
    Nombre(id=3, nombre="Pedro", apellido="Rodríguez", edad=40)
]

@app.get("/nombres", response_model=list[Nombre])
async def obtener_nombres():
    return nombres

@app.post("/nombres", response_model=Nombre)
async def agregar_nombre(nombre: Nombre):
    nombre.id = len(nombres) + 1  # Asignar un ID único
    nombres.append(nombre)
    return nombre

@app.delete("/nombres/{nombre_id}", response_model=Nombre)
async def eliminar_nombre(nombre_id: int):
    nombre = next((n for n in nombres if n.id == nombre_id), None)
    if nombre:
        nombres.remove(nombre)
        return nombre
    raise HTTPException(status_code=404, detail="Nombre no encontrado")
