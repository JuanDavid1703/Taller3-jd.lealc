from models.animal_exotico import Animal_exotico

class Boa(Animal_exotico):
    def __init__(self, nombre: str, edad: int, peso: int, pais_origen: str,impuestos: float) -> None:
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self._cant_ratones=0
    
    def hacer_sonido(self) -> None:
        return "Tsssss"
    
    def agregar_raton(self, cant_raton:int)->str:
        if self._cant_ratones +cant_raton < 20 and self._cant_ratones<20:
            self._cant_ratones += cant_raton
            return "Exito!!"
        elif self._cant_ratones +cant_raton >= 20 and self._cant_ratones<20:
            aux= self._cant_ratones
            self._cant_ratones = 20
            return f"La boa solo puede comer {20-aux} ratones"
        else:
            return "¡La boa está llena!"
    
    def obtener_cant_raton(self)->int:
        return self._cant_ratones
