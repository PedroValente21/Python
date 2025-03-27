def funcao():
    variavel = 1
    if variavel == 1:
        raise Exception("Pode ser um não doidão")

try:
    funcao()
except Exception as e:
    print("Deu pau esse trein aqui ó:", e)
