from abc import ABC, abstractmethod

## _variable para usar como herencia, __variable para hacrela privada 
#Se puede colocar la librería dentro de los paréntesis de la clase creada, permite usar los métodos de la librearía en la clase
class IAnimal(ABC):
    @abstractmethod
    def comer(self, kilos:int):
        pass
    
    @abstractmethod
    def obtener_kilos_comidos(self):
        pass 
    