def ola_mundo(nome, sobreNome):
    print('Olá,', nome)
    nomeCompleto = nome + " " + sobreNome
    return nomeCompleto

nome = "Pedro"
sobreNome = "Valente"
nomeCompleto = ola_mundo(nome, sobreNome)
print(nomeCompleto)

quadrado = lambda x: x ** 2
print(quadrado(5))