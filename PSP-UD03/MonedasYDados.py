import random
from pprint import pprint

from matplotlib import pyplot as plt

# Declaración del diccionario
libroDeDiccionarios = {"Resultado": {
    "Moneda": {
        "vecesCaras": {
        },
        "vecesCruces": {
        }
    },
    "ResultadoDados": {
    }
}
}

# Variables globales que utilizaremos:
moneda = ["cara", "cruz"]
DESDE = 1
HASTA = 6 + 1
dado = [x for x in range(DESDE, HASTA)]
nVeces = 1_000_000
ntiradas = 10
cuantasVecesTiramosDadosPorExperimento = 3

# Inicialización de los diccionarios
# Las variables no funcionan en el rango
for x in range(11):
    libroDeDiccionarios["Resultado"]["Moneda"]["vecesCaras"][x] = 0
    libroDeDiccionarios["Resultado"]["Moneda"]["vecesCruces"][x] = 0

for x in range(3, 19):
    libroDeDiccionarios["Resultado"]["ResultadoDados"][x] = 0


# Función para tirar la moneda el numero de veces que decidamos
def tirarMoneda():
    caras = 0
    cruces = 0
    for _ in range(ntiradas):
        tirada = random.choice(moneda)
        if tirada == "cara":
            caras += 1
        else:
            cruces += 1
    libroDeDiccionarios["Resultado"]["Moneda"]["vecesCaras"][caras] += 1
    libroDeDiccionarios["Resultado"]["Moneda"]["vecesCruces"][cruces] += 1


# Cogemos los resultados de los dados,
# y los añadimos en el diccionario correspondiente.
def resultadoDados():
    sum = 0
    for _ in range(cuantasVecesTiramosDadosPorExperimento):
        tirada = random.choice(dado)
        sum += tirada
    libroDeDiccionarios["Resultado"]["ResultadoDados"][sum] += 1


# Creación de función de impresión de la grafica de caras
def imprimirGraficaCaras():
    plt.figure()
    claveCara = libroDeDiccionarios["Resultado"]["Moneda"]["vecesCaras"].keys()
    valorCara = libroDeDiccionarios["Resultado"]["Moneda"]["vecesCaras"].values()
    plt.plot(claveCara, valorCara)
    plt.title("Monedas-cara")
    plt.xlabel("Ocurrencias")
    plt.show()


# Creación de función de impresión de la grafica de cruces
def imprimirGraficaCruces():
    plt.figure()
    claveCruz = libroDeDiccionarios["Resultado"]["Moneda"]["vecesCruces"].keys()
    valorCruz = libroDeDiccionarios["Resultado"]["Moneda"]["vecesCruces"].values()
    plt.plot(claveCruz, valorCruz)
    plt.title("Monedas-Cruz")
    plt.xlabel("Ocurrencias")
    plt.show()


# Creación de función de impresión de la grafica de dados
def imprimirGraficaDados():
    plt.figure()
    num = libroDeDiccionarios["Resultado"]["ResultadoDados"].keys()
    numveces = libroDeDiccionarios["Resultado"]["ResultadoDados"].values()
    plt.plot(num, numveces)
    plt.title("Monedas-Cruz")
    plt.xlabel("Ocurrencias")
    plt.show()


# Realizamos la función de main
if __name__ == '__main__':
    for _ in range(nVeces):
        # Utilizamos las funciones nveces que queremos hacer el experimento
        resultadoDados()
        tirarMoneda()

    # Mostramos el diccionario principal
    pprint(libroDeDiccionarios)

    # Llamamos a la funcioón imprimirGraficaDados
    imprimirGraficaDados()
