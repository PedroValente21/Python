print("Olá, Mundo!")
var1 = 10
var2 = 20  

for i in range(50):
    if i % 2 == 0:
        print(i)
        var1 += 1
    elif i == 11:
        print("i é igual a 11")
    elif i == 15:
        pass
    elif i == 17:
        break
    else:
        print("i não tem condicinal pra isso")
        var2 * 10

print(var2, var1)
    