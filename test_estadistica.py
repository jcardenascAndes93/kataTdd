from unittest import TestCase
from Estadistica import Estadistica


class EstadisticaTest(TestCase):    

    def test_calcularElementosYMinimoCadenaVacia(self):
        self.assertEqual(Estadistica.calcularEstadistica(""),
                         [0, 0], "Cadena vacia")
