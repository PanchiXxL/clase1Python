#Encontrar perimetro de un circulo

#Transformar grados farenheit a celcius

#Formula General

#Area de un trangulo

from math import pi
import math


class Operaciones:
    def __init__(self,a,b,c,d):
        self.valor1 = a
        self.valor2 = b
        self.valor3 = c
        self.valor4 = d


class Area(Operaciones):
    def circulo(self):
        area = pi * self.valor1 ** 2
        print("El area del circulo es: {:.4}".format(area))
        
class Farenehit(Operaciones):
    def grados(self):
        celcius = ((self.valor2-32)/1.8)
        print("El grado celcius es: {:.4}".format(celcius))

class FormulaG(Operaciones):
    def Formula_General(self):
        x1 = (-self.valor2 + math.sqrt((self.valor2**2)-(4*self.valor1*self.valor3)))/(2*self.valor1)
        x2 = (-self.valor2 - math.sqrt((self.valor2**2)-(4*self.valor1*self.valor3)))/(2*self.valor1)
        print("Valor de X1: ",x1)
        print("Valor de X2: {:.3}".format(x2))

class Triangulo(Operaciones):
    def AreaTriangulo(self):
        areaTrangulo = (self.valor4*self.valor1)/2
        print("Area del triangulo es: ",areaTrangulo)
        



circulo = Area(5, pi, 0, 0)
circulo.circulo()

grados = Farenehit(0, 9, 0, 0)
grados.grados()

formula = FormulaG(3, -5, 2, 0)
formula.Formula_General()

areaT = Triangulo(3, -5, 2, 1)
areaT.AreaTriangulo()


        
