### Juan David Leal Campuzano

from models.boa import Boa
from models.huron import Huron
from guarderia import Guarderia

boa1=Boa(nombre="Juan",edad=2,peso=25,pais_origen="India",impuestos=2550)
huron1=Huron("Huroncillo",12,20,"Hurozones","Mongolia", 2300)    
boa2=Boa(nombre="Abrazadora",edad=5, peso=15,pais_origen="Colombia",impuestos=2800)
boa3=Boa(nombre="Tsiseadora",edad=20, peso=145,pais_origen="Brasil",impuestos=5600)
huron2=Huron("Resgunios",6, 10,"Lampiño","Mexico",2600)

guarderia1=Guarderia(nombre="Los traficantes",ubicacion="Las malvinas")
guarderia1.agregar_animales(boa1)
guarderia1.agregar_animales(animal=boa2)
guarderia1.agregar_animales(animal=huron1)
guarderia1.agregar_animales(animal=huron2)


print(guarderia1.alimentar_boa(2,boa1))
print("Cantidad de ratones: ",boa1.obtener_cant_raton())

print(guarderia1.alimentar_boa(6,boa1))
print("Cantidad de ratones: ",boa1.obtener_cant_raton())

print(guarderia1.alimentar_boa(1,boa1))
print("Cantidad de ratones: ",boa1.obtener_cant_raton())

print(guarderia1.alimentar_boa(12,boa1))
print("Cantidad de ratones: ",boa1.obtener_cant_raton())

print(guarderia1.alimentar_boa(12,boa1))
print(guarderia1.alimentar_boa(1,boa1))
