from models.animal import Animal
from abc import ABC, abstractmethod

class Animal_exotico(Animal,ABC):
    def __init__(self,nombre:str, edad:int, peso:int, pais_origen: str, impuestos: float) -> None:
        ### cuando se llaman los parámetros heredados de una clase padre, se debe respetar el orden de las variables en la clase padre
        super().__init__(nombre, edad, peso)
        self._pais_origen=pais_origen
        self._impuestos=impuestos
    
    def obtener_pais_origen(self)->str:
        return self._pais_origen
    
    def obtener_impuestos(self) -> float:
        return self._impuestos
    
    def calcular_flete(self)->float:
        return self._peso * self._impuestos
    
    @abstractmethod
    def hacer_sonido(self) -> None:
        pass