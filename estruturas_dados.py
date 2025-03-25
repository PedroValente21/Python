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
print(quadrados)  # Imprime [4, 16]
    