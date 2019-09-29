from unittest import TestCase
from Estadistica import Estadistica


class EstadisticaTest(TestCase):

    def test_calcularElemMinMaxCadenaVacia(self):
        self.assertEqual(Estadistica.calcularEstadistica(""),
                         [0, 0, 0], "Cadena vacia")

    def test_calcularElemMinMaxCadenaConUnNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica("3"),
                         [1, 3, 3], "Un numero")

    def test_calcularElemMinMaxCadenaConDosNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica("3,2"),
                         [1, 2, 3], "Dos numeros")
