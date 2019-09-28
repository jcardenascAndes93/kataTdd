_author_ = 'Elkin Mantilla, Juan Camilo Cardenas'


class Estadistica:
    def calcularEstadistica(cadena):
        if cadena == "":
            return [0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            minimo = int(numeros[0])
            for n in numeros:
                if minimo > int(n):
                    minimo = int(n)
            return [len(numeros), minimo]
        else:
            return [1, int(cadena)]
