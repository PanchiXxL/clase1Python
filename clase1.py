print ("hola mundo")
a = int(input("Ingrese inicio: "))

b = int(input("Ingrese fin: "))

c = int(input("Ingrese valor para la table de multiplicar"))

for i in range(a,b):
    mult = i*c
    print(i," * ",c," = ",mult)