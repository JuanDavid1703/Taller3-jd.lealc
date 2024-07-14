from animal import Animal

class Perro(Animal):
    def __init__(self, nombre: str, edad: int, peso: int, raza: str, concentrado: str) -> None:
        super().__init__(nombre, edad, peso)
        self.__raza=raza
        self.__concentrado=concentrado
    
    def obtener_raza(self)->None:
        return self.__raza
    
    def hacer_sonido(self) -> None:
        return "Guauu Guauuu"
    
    def moverse(self) -> None:
        return "Corriendo"
    
    def obtener_concnetrado_favorito(self)->None:
        return self.__concentrado