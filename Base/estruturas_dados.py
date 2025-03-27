lista = ["Cruzeiro", "Atlético", "América", "Villa Nova", "Caldense"]
for time in lista:
    print(time)

print(lista[0], lista[0], "querido, tão combatido jamais vencido.")
print()

lista.append("Coimbra")
print(lista)
lista.insert(2, "Uberlândia")
print(lista)
lista.remove("Villa Nova")
print(lista)
franga = lista.pop(1)
print(franga)
lista.sort()
print(lista)
lista.reverse()
print(lista)

números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  

print()

tupla = (1, 2, 3, 4, 5, 4)
print(tupla.count(4))
print(tupla.index(4))

print()

dicionario = {"Cruzeiro": 6, "Atlético": 1, "América": 2, "Villa Nova": 5, "Caldense": 7}
print ("Copas do Brasil do Cruzeiro -", dicionario["Cruzeiro"])
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
dicionario.update({"Coimbra": 0}) 
print(dicionario)

print()

conjuntoN = {1, 2, 0, 5}
conjuntoZ = set({-3, -2, -1, 0, 1, 2})
conjuntoN.add(3)
conjuntoZ.remove(-3)
print(conjuntoN.union(conjuntoZ))
print(conjuntoN.intersection(conjuntoZ))
print(conjuntoN.difference(conjuntoZ))
print(conjuntoZ.difference(conjuntoN))
print(conjuntoN.symmetric_difference(conjuntoZ))
conjuntoN.clear()
print(conjuntoN)


