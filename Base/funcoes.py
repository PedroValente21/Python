import math


def ola_mundo(nome, sobreNome):
    print('Olá,', nome,'Torcedor do', time)
    nomeCompleto = nome + " " + sobreNome
    return nomeCompleto

def somaNumeros(*nuemeros):
    soma = 0
    for numero in nuemeros:
        soma += numero
    return soma


time = "Cruzeiro"
nome = "Pedro"
sobreNome = "Valente"
nomeCompleto = ola_mundo(nome, sobreNome)
print(nomeCompleto)

quadrado = lambda x: x ** 2
print(quadrado(5))
print(somaNumeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calcula_raiz_quadrada(numero):
    return math.sqrt(numero)