#-------------------------------------
# 1
from ntpath import join
from operator import contains, index
import string
from pkg_resources import compatible_platforms

from psutil import cpu_times


thirty='Thirty'
days='Days'
of='Of'
python='Python'

contact_string=thirty+' '+days+' '+of+' '+python
print(contact_string) # Concatenando strings usando '+' 

old_format_string='%s %s %s %s'%(thirty,days,of,python)
print(old_format_string) # Forma antigua de concatenar 

new_format_string='{} {} {} {}'.format(thirty,days,of,python)
print(new_format_string) # Nueva forma de concatenar

print(f'{thirty} {days} {of} {python}') # Interpolacion de string (f-strings - py3.6+)

#-------------------------------------
# 2
coding='Coding'
var_for='For'
all='All'
cfa='Cofing For All'

contact_string=coding+' '+var_for+' '+all
print(contact_string)

old_format_string='%s %s %s'%(coding,var_for,all)
print(old_format_string)

new_format_string='{} {} {}'.format(coding,var_for,all)
print(new_format_string)

print(f'{coding} {var_for} {all}')

#-------------------------------------
# 3
company='Coding For All'

#-------------------------------------
# 4
print(company)

#-------------------------------------
# 5
print(len(company)) # Longitud del string

#-------------------------------------
# 6
print(company.upper()) # Todo en mayusculas

#-------------------------------------
# 7
print(company.lower()) # Todo en minusculas

#-------------------------------------
# 8
print('Coding For All'.capitalize()) # Primera letra de primer palabra en mayusculas
print('Coding For All'.title()) # Primera letra de cada palabra en mayusculas
print('Coding For All'.swapcase()) # Invierte mayusculas y minusculas

#-------------------------------------
# 9 
print(company[0:company.index(' ')])
print(company[0:company.find(' ')])
# index y find devuelven la posicion de la primera ocurrencia

#-------------------------------------
# 10
print(company.find('Coding'))
print(company.index('Coding'))
print(contains(company,'Coding')) # contains(contenedor,contenido)
print('Coding' in company) # contenido in contenedor

#-------------------------------------
# 11
print(company.replace('Coding','Python')) # string.replace(original,reemplazo)

#-------------------------------------
# 12
python_for_everyone='Python For Everyone'
print(python_for_everyone.replace('Everyone','all'))

#-------------------------------------
# 13
print(company.split(' ')) # Corta el string donde se indique, devuelve una lista?

#-------------------------------------
# 14
var_company="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(var_company.split(','))

#-------------------------------------
# 15
print(cfa[0])

#-------------------------------------
# 16
print(len(cfa)-1)

#-------------------------------------
# 17
print(cfa[10])

#-------------------------------------
# 18
def acronym(string):
    acronimo=''
    for letra in string:
        if letra.isupper():
            acronimo=acronimo+letra
    return acronimo

acro_pfe=acronym(python_for_everyone)
print(acro_pfe)

#-------------------------------------
# 19
acro_cfa=acronym(company)
print(acro_cfa)

#-------------------------------------
# 20
print(company.index('C'))

#-------------------------------------
# 21
print(company.index('F'))

#-------------------------------------
# 22
print(company.rindex('l'))

#-------------------------------------
# 23
string_falopa='You cannot end a sentence with because because because is a conjunction'
print(string_falopa.find('because'))
print(string_falopa.index('because'))

#-------------------------------------
# 24
print(string_falopa.rindex('because'))
print(string_falopa.rfind('because'))

#-------------------------------------
# 25 y 27
print(string_falopa[0:string_falopa.index('because')]+string_falopa[string_falopa.rindex('is'):])

#-------------------------------------
# 26
print(string_falopa.find('because'))

#-------------------------------------
# 28
print(company.startswith('Coding')) # String comienza con...

#-------------------------------------
# 29
print(company.endswith('coding')) # String termina con...

#-------------------------------------
# 30
print('   Coding For All      '.strip()) # Remueve tabs del principio y final
print('   Coding For All      '.lstrip()) # Remueve tabs del principio (left)
print('   Coding For All      '.rstrip()) # Remueve tabs del final (right)

#-------------------------------------
# 31
var1='30DaysOfPython'
var2='thirty_days_of_python'
print(var1.isidentifier())
print(var2.isidentifier())

#-------------------------------------
# 32
python_lib=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(python_lib)) # Concatena una lista en un string separado por lo que indiquemos

#-------------------------------------
# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

#-------------------------------------
# 34
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'.expandtabs(10))
# Expandimos de 8 a 10 espacios por tab

#-------------------------------------
# 35
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square')

#-------------------------------------
# 36
ocho=8
seis=6
print(f'{ocho} + {seis} = {ocho+seis}')
print(f'{ocho} - {seis} = {ocho-seis}')
print(f'{ocho} * {seis} = {ocho*seis}')
print(f'{ocho} / {seis} = {"{:.2f}".format(ocho/seis)}') # Formateo a 2 decimales
print(f'{ocho} % {seis} = {ocho%seis}')
print(f'{ocho} // {seis} = {ocho//seis}')
print(f'{ocho} ** {seis} = {ocho**seis}')
