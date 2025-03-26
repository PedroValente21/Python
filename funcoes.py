def ola_mundo(nome, sobreNome):
    print('Olá,', nome)
    nomeCompleto = nome + " " + sobreNome
    return nomeCompleto

nome = "Pedro"
sobreNome = "Valente"
nomeCompleto = ola_mundo(nome, sobreNome)
print(nomeCompleto)