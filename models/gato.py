from animal import Animal

class Gato(Animal):
    def __init__(self, nombre: str, edad: int, peso: int, raza: str) -> None:
        super().__init__(nombre, edad, peso)
        self.__raza=raza
    
    def obtener_raza(self)->None:
        return self.__raza
    
    def hacer_sonido(self) -> None:
        return "Miauuu Miauuu"
    
    def moverse(self) -> None:
        return "Corriendo"
    
    def dar_nombre(self, nombre:str)->str:
        self._nombre=nombre