from models.huron import Huron
import unittest


class Test_perro(unittest.TestCase):
    def test_hacer_sonido(self):
        huron1=Huron("Rufo",12, 5,"Aleman","Alemania",2500)
        self.assertEqual(huron1.hacer_sonido(),"Eek Eek")

    def test_calcular_flete(self):
        huron1=Huron("Rufo",12, 5,"Aleman","Alemania",2500)
        self.assertEqual(huron1.calcular_flete(),5*2500)

if __name__=="__main__":
    unittest.main()