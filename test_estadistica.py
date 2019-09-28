from unittest import TestCase
from Estadistica import Estadistica


class EstadisticaTest(TestCase):
    def test_calcularElementosCadenaVacia(self):
        self.assertEqual(Estadistica.calcularEstadistica(""),
                         [0], "Cadena vacia")

    def test_calcularElementosCadenaConUnNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica("1"),
                         [1], "Un numero")
        self.assertEqual(Estadistica.calcularEstadistica("2"),
                         [1], "Un numero")
        self.assertEqual(Estadistica.calcularEstadistica(
            "10"), [1], "Un numero")

    def test_calcularElementosCadenaConDosNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica(
            "1,2"), [2], "Dos numero")

    def test_calcularElementosCadenaConNNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica(
            "1,2,4,5"), [4], "N numero")
    
    def test_calcularElementosYMinimoCadenaVacia(self):
        self.assertEqual(Estadistica.calcularEstadistica(""),
                         [0, 0], "Cadena vacia")
