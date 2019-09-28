_author_ = 'Elkin Mantilla, Juan Camilo Cardenas'


class Estadistica:
    def calcularEstadistica(cadena):
        if cadena == "":
            return [0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros)]
        else:
            return [1, int(cadena)]
