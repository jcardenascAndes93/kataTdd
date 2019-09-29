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
                         [2, 2, 3], "Dos numeros")

    def test_calcularElemMinMaxCadenaConNNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica("3,2,4,8,10"),
                         [5, 2, 10], "N numeros")
