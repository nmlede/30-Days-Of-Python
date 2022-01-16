#Level 1
#3
nombre = 'Nicolas'
#4
apellido = 'Marinucci'
#5
nombre_completo = 'Nicolas Marinucci'
#6
pais = 'Argentina'
#7
ciudad = 'La Rioja'
#8
edad = 33
#9
año = 2022
#10
esta_casado = False
#11
es_verdad = True
#12
brilla = False

#Level 2
#1
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(ciudad))
print(type(pais))
print(type(edad))
print(type(año))
print(type(esta_casado))
print(type(es_verdad))
print(type(brilla))
#2
print(len(nombre))
#3
print(len(nombre)==len(apellido))
print(len(nombre)!=len(apellido))
print(len(nombre)<len(apellido))
print(len(nombre)>len(apellido))
#4
num1, num2, num3, num4, num5 = 1,2,3,4,5
#4.1
suma = num1 + num2
print(suma)
#4.2
resta = num1 - num2
print(resta)
#4.3
multi = num1 * num2
print(multi)
#4.4
division = float(num1/num2)
print(division)
#4.5
modulo = float(num1%num2)
print(modulo)
#4.6
potencia = num1**num2
print(potencia)
#4.
div_piso = num1 // num2
#5
nombre = input("Ingresa un nombre: ")
apellido = input('Ingrese un apellido: ')
print('Mi nombre es '+nombre+' '+apellido)

