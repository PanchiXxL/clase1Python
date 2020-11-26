'''print ("hola mundo")
a = int(input("Ingrese inicio: "))

b = int(input("Ingrese fin: "))

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

                ARREGLOS


format -> sirve para una concatenacion 
insert -> nos permite insertar un valor en cualquier parte deun arreglo  
len -> permite ver la cantidad de datos de un vector             
                

n = int(input("Ingrese dimension del vector: "))

vect = []
for i in range(0, n):
    valor = int(input("ingrese valores: ").format(i))
    vect.append(valor)
print("Los valores ingresados son")

for i in range (0, n):
    print("[ ",i," ]",vect[i])

print("ingrese nuevos elementos en el arreglo: ")
vect.insert(2,10)
print("valores finales son: ")
for i in range(0, len(vect)):
    print("[ ",i," ]",vect[i])
    
    POOOO
    '''

class persona:
    nombre = input("Ingrese nombre: ")
    sueldo = float(input("Ingrese sueldo: "))
    pass
empleado = persona()


valorfin = ((empleado.sueldo)*0.12)
valorFinal = empleado.sueldo + valorfin
print("Nombre empleado: ", empleado.nombre)
print("sueldo principal: ", empleado.sueldo)
print("valor de incremento: ", valorfin)
print("Sueldo final: ", valorFinal)



