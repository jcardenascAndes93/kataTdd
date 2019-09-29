_author_ = 'Elkin Mantilla, Juan Camilo Cardenas'


class Estadistica:
    def calcularEstadistica(cadena):
        if cadena == "":
            return [0, 0, 0, 0]
        elif "," in cadena:
            numeros = cadena.split(",")
            minimo = int(numeros[0])
            maximo = int(numeros[0])
            for n in numeros:
                if int(n) > maximo:
                    maximo = int(n)
                if minimo > int(n):
                    minimo = int(n)
            return [len(numeros), minimo, maximo]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]
