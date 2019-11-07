import unittest

from interfaz_sudoku import interfaz

from parameterized import parameterized

class Test_interfaz(unittest.TestCase):
    
    def test_validar(self):
        nombre = interfaz()
        self.assertTrue (nombre.validar(5,8,1))

    @parameterized.expand([(1.5,"a","c"), (5,"o","C"), (7,5,"s"), ("q",8,9), (10,11,12), ("l","m","n"), ("a",5,"b")])
    def test_validar_falso(self,fila,columna,numero):
        nombre = interfaz()
        self.assertFalse (nombre.validar(fila,columna,numero))

   






if __name__ == '__main__':
    unittest.main()