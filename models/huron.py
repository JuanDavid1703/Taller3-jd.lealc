from models.animal_exotico import Animal_exotico

class Huron(Animal_exotico):
    def __init__(self, nombre: str, edad: int, peso: int, raza: str, pais_origen: str,impuestos: float) -> None:
        super().__init__(nombre, edad, peso,pais_origen,impuestos)
        self.__raza=raza
    
    def hacer_sonido(self) -> None:
        return "Eek Eek"
    