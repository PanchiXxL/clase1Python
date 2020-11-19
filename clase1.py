print ("hola mundo")
'''a = int(input("Ingrese inicio: "))

b = int(input("Ingrese fin: "))'''

c = int(input("Ingrese valor para la table de multiplicar: "))
cont=0
d=0
for i in range(1,11):
    mult = i*c
    d+=mult
    if (i%2==0):
        print(i," * ",c," = ",mult)
        cont+=mult
        
print("la suma de las respuestas pares es: ",cont)
print("Suma total: ",d)


