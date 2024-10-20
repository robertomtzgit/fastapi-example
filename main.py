from fastapi import FastAPI, HTTPException
from models import Nombre

app = FastAPI()

# Lista inicial de nombres
nombres = [
    Nombre(id=1, nombre="Juan", apellido="Pérez", edad=30),
    Nombre(id=2, nombre="María", apellido="Gómez", edad=25),
    Nombre(id=3, nombre="Pedro", apellido="Rodríguez", edad=40),
    Nombre(id=4, nombre="Ana", apellido="Fernández", edad=28),
    Nombre(id=5, nombre="Luis", apellido="Martínez", edad=35),
    Nombre(id=6, nombre="Laura", apellido="Sánchez", edad=22),
    Nombre(id=7, nombre="Carlos", apellido="López", edad=45),
    Nombre(id=8, nombre="Sara", apellido="Ramírez", edad=33),
    Nombre(id=9, nombre="Jorge", apellido="Torres", edad=50),
    Nombre(id=10, nombre="Claudia", apellido="Hernández", edad=29)
]

@app.get("/nombres", response_model=list[Nombre])
async def obtener_nombres():
    return nombres

@app.get("/nombres/{nombre_id}", response_model=Nombre)
async def obtener_nombre(nombre_id: int):
    nombre = next((n for n in nombres if n.id == nombre_id), None)
    if nombre:
        return nombre
    raise HTTPException(status_code=404, detail="Nombre no encontrado")

@app.post("/nombres", response_model=Nombre)
async def agregar_nombre(nombre: Nombre):
    nuevo_id = len(nombres) + 1  # Genera un nuevo ID
    nombre.id = nuevo_id  # Asigna el nuevo ID al nombre
    nombres.append(nombre)
    return nombre

@app.delete("/nombres/{nombre_id}", response_model=Nombre)
async def eliminar_nombre(nombre_id: int):
    nombre = next((n for n in nombres if n.id == nombre_id), None)
    if nombre:
        nombres.remove(nombre)
        return nombre
    raise HTTPException(status_code=404, detail="Nombre no encontrado")
