from unittest import TestCase
from Estadistica import Estadistica


class EstadisticaTest(TestCase):

    def test_calcularElemMinMaxCadenaVacia(self):
        self.assertEqual(Estadistica.calcularEstadistica(""),
                         [0, 0, 0], "Cadena vacia")

    def test_calcularElemMinMaxCadenaConUnNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica("1"),
                         [1, 1, 1], "Cadena vacia")
