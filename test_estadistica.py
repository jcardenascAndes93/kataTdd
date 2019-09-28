from unittest import TestCase
from Estadistica import Estadistica


class EstadisticaTest(TestCase):

    def test_calcularElementosYMinimoCadenaVacia(self):
        self.assertEqual(Estadistica.calcularEstadistica(""),
                         [0, 0], "Cadena vacia")

    def test_calcularElementosYMinimoUnNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica("3"),
                         [1, 3], "Un numero")
    
    def test_calcularElementosYMinimoDosNumeros(self):
        self.assertEqual(Estadistica.calcularEstadistica("3, 1"),
                         [2, 1], "Un numero")
        self.assertEqual(Estadistica.calcularEstadistica("3, 11"),
                         [2, 3], "Un numero")