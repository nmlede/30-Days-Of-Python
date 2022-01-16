#1
edad = 33
#2
altura = 1.65
#3
complejo = 1j

#4
def area_triangulo():
    base = float(input('Ingresa la base: '))
    altura = float(input('Ingresa la altura: '))
    return (0.5 * base * altura)

area = area_triangulo()
print(area)

#5
def perimetro_triangulo():
    lado_a = int(input('Ingrese el lado A: '))
    lado_b = int(input('Ingrese el lado B: '))
    lado_c = int(input('Ingrese el lado C: '))
    return (lado_a + lado_b + lado_c)

perimetro = perimetro_triangulo()
print(perimetro)

#6
