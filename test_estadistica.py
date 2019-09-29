from unittest import TestCase
from Estadistica import Estadistica


class EstadisticaTest(TestCase):

    def test_calcularElemMinMaxPromCadenaVacia(self):
        self.assertEqual(Estadistica.calcularEstadistica(""),
                         [0, 0, 0, 0], "Cadena vacia")

    def test_calcularElemMinMaxPromUnNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica("8"),
                         [1, 8, 8, 8], "Un numero")

    def test_calcularElemMinMaxPromDosNumeros(self):
        self.assertEqual(Estadistica.calcularEstadistica("8, 2"),
                         [2, 2, 8, 5], "Dos numeros")

    def test_calcularElemMinMaxPromNNumeros(self):
        self.assertEqual(Estadistica.calcularEstadistica("8, 2, 4, 6"),
                         [2, 2, 8, 5], "Dos numeros")