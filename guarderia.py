from models.boa import Boa
from models.huron import Huron

class Guarderia():
    def __init__(self, nombre:str, ubicacion: str) -> None:
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._animales=[]
            
    def obtener_nombre(self)->str:
        return self._nombre
    
    def obtener_ubicacion(self)->str:
        return self._ubicacion
    
    def agregar_animales(self, animal)->None:
        self._animales.append(animal)
    
    def alimentar_huron(self, kilos:int)->None:
        Huron.comer(kilos=kilos)
    
    def obtener_animales(self)->list:
        return self._animales
      
    def alimentar_boa(self, cant_ratones:int,boa:Boa)->str:
        
        try:    
            if boa not in self._animales:
                raise ValueError("Esta boa no existe!")

            else:
                raise ValueError(boa.agregar_raton(cant_ratones))
                    
        except ValueError as e:
            return e
