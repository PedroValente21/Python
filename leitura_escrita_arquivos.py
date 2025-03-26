arquivo = open("arquivo.txt", "r")  
print(arquivo.read())
arquivo.close()

arquivo = open("arquivo.txt", "w")  
arquivo.write("Que mora dentro do meu coração --- Texto adiconado pelo programa")
arquivo.close()