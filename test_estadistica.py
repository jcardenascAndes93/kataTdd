from unittest import TestCase
from Estadistica import Estadistica

class EstadisticaTest(TestCase):
    def test_calcularElementosCadenaVacia(self):
        self.assertEqual(Estadistica.calcularEstadistica(""),0,"Cadena vacia")

    def test_calcularElementosCadenaConUnNumero(self):
        self.assertEqual(Estadistica.calcularEstadistica("1"), 1, "Un numero")
        self.assertEqual(Estadistica.calcularEstadistica("2"), 1, "Un numero")
        self.assertEqual(Estadistica.calcularEstadistica("10"), 1, "Un numero")


