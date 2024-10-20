from pydantic import BaseModel, Field
from typing import Annotated

class Nombre(BaseModel):
    id: int
    nombre: Annotated[str, Field(min_length=2, max_length=50)]
    apellido: Annotated[str, Field(min_length=2, max_length=50)]
    edad: Annotated[int, Field(ge=0, le=120)]  # Edad entre 0 y 120 años
