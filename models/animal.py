from models.ianimal import IAnimal
from abc import ABC, abstractmethod

## _variable para usar como herencia, __variable para hacerla privada 
#Se puede colocar la librería dentro de los paréntesis de la clase creada, permite usar los métodos de la librearía en la clase
class Animal(IAnimal,ABC):
    def __init__(self, nombre:str, edad:int, peso:int) -> None:
        self._nombre=nombre
        self._edad=edad
        self._peso=peso
        self._kilos_comidos=0
    
    def obtener_nombre(self)-> str:
        return self._nombre
    
    def obtener_peso(self)-> int:
        return self._peso
    
    def obtener_edad(self)-> int:
        return self._edad
    
    def comer(self, kilos:int)-> None:
        self._kilos_comidos += kilos
    
    def obtener_kilos_comidos(self)-> int:
        return self._kilos_comidos
        
    # @abstractmethod No permite utilizar el método por el abstrac method, debe estar arriba de la función creada
    @abstractmethod
    def hacer_sonido(self)->None:
        pass

