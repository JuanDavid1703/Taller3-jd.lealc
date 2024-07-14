from models.boa import Boa
import unittest


class Test_perro(unittest.TestCase):
    def test_hacer_sonido(self):
        boa1=Boa(nombre="Rufo",edad=12, peso=20,pais_origen="Perú",impuestos=3500)
        self.assertEqual(boa1.hacer_sonido(),"Tsssss")
    
    def test_calcular_flete(self):
        boa1=Boa(nombre="Rufo",edad=12, peso=20,pais_origen="Perú",impuestos=3500)
        self.assertEqual(boa1.calcular_flete(),20*3500)
    
    def test_agregar_raton(self):
        boa1=Boa(nombre="Rufo",edad=12, peso=20,pais_origen="Perú",impuestos=3500)
        cant_ratones=boa1._cant_ratones
        if cant_ratones> 10:
            self.assertEqual(boa1.agregar_raton(cant_raton=cant_ratones), "Demasiados Ratones!")
        else:
            self.assertEqual(boa1.agregar_raton(cant_raton=cant_ratones), "Alimentado")

if __name__=="__main__":
    unittest.main()