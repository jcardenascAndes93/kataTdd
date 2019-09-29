from unittest import TestCase
from Estadistica import Estadistica


class EstadisticaTest(TestCase):

    def test_calcularElemMinMaxPromCadenaVacia(self):
        self.assertEqual(Estadistica.calcularEstadistica(""),
                         [0, 0, 0, 0], "Cadena vacia")

    def test_calcularElemMinMaxPromUnNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica("8"),
                         [1, 8, 8, 8], "Cadena vacia")
