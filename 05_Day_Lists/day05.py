# Exercises: Day 5

# Exercises: Level 1
# 1 Declare an empty list
from itertools import count
from struct import unpack


lst_vacia=list()
lst_vacia_array=[]

# 2 Declare a list with more than 5 items
lst_frutas=['manzana','banana','pera','durazno','anana']

# 3 Find the length of your list
print(len(lst_frutas))

# 4 Get the first item, the middle item and the last item of the list
print(lst_frutas[0])
print(lst_frutas[int(len(lst_frutas)/2)])
print(lst_frutas[len(lst_frutas)-1])

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type=['Nicolas',33,1.65,'Soltero','Mi Casa']

# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

# 7 Print the list using print()
print(mixed_data_type)
print(it_companies)

# 8 Print the number of companies in the list
print(len(it_companies))

# 9 Print the first, middle and last company
print(it_companies[0])
print(it_companies[int(len(it_companies)/2)])
print(it_companies[len(it_companies)-1])

# 10 Print the list after modifying one of the companies
it_companies[0]='Twitter'
print(it_companies)

# 11 Add an IT company to it_companies
it_companies.append('Facebook') ## Agrega elemento al final
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies)/2),'Tsoft')
print(it_companies)

# 13 Change one of the it_companies names to uppercase (IBM excluded!)
index=it_companies.index('Tsoft') # Encuentro el indice de la compania
it_companies[index]=it_companies[index].upper() # reemplazo el valor
print(it_companies)

# 14 Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

# 15 Check if a certain company exists in the it_companies list.
print('Oracle' in it_companies)
print('Morcilla' in it_companies)

# 16 Sort the list using sort() method
print(it_companies.sort()) # Ordena alfabeticamente.

# 17 Reverse the list in descending order using reverse() method
it_companies.reverse() # Invierte el orden
print(it_companies) 

# 18 Slice out the first 3 companies from the list
print(it_companies[0:3]) # El slice es desde (incluido) hasta (no incluido)
print(it_companies[3:])

# 19 Slice out the last 3 companies from the list
print(it_companies[-3:])
print(it_companies[:-3])

# 20 Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies)//2])

# 21 Remove the first IT company from the list
print(it_companies)
print(it_companies.pop(0))
print(it_companies)

# 22 Remove the middle IT company or companies from the list
print(it_companies)
print(it_companies.pop(len(it_companies)//2))
print(it_companies)

# 23 Remove the last IT company from the list
print(it_companies)
print(it_companies.pop(len(it_companies)-1))
print(it_companies)

# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25 Destroy the IT companies list
del it_companies

# 26 Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable 
# full_stack. Then insert Python and SQL after Redux.
front_end=['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end=['Node','Express', 'MongoDB']
front_end=front_end+back_end # Join es concatenar listas
print(front_end)

full_stack=front_end.copy() # copia una lista/array
print(full_stack)



# Exercises: Level 2
# The following is a list of 10 students ages:
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1 Sort the list and find the min and max age
ages.sort() # la lista se ordena y se almacena en la misma variable original
print(ages)
print(f'La edad menor es: {ages[0]}, y la edad mayor es: {ages[-1]}')

def find_ages(lista):
    min_age=lista[0]
    max_age=lista[0]
    for idx in range(1, len(lista)):
        if lista[idx-1] > lista[idx]: # Usar idx-1 para no tener error de out of range
            min_age=lista[idx]
        if lista[idx-1] < lista[idx]:
            max_age=lista[idx]
    
    return min_age,max_age # retorna dos valores

min_age,max_age=find_ages(ages) # declaro dos variables a las que se les asignan
# los valores retornados en orden.

print(f'La menor edad es: {min_age}, y la mayor edad es: {max_age}')

# 2 Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(f'Lista con elementos agregados {ages}')

# 3 Find the median age (one middle item or two middle items divided by two)
# INVESTIGAR A QUE SE REFIERE EL PUNTO

# 4 Find the average age (sum of all items divided by their number) PROMEDIO
ages.sort()
sum_ages=sum(ages)
prom_ages=sum_ages//len(ages)
print(f'El promedio de edad es de: {prom_ages}')

# 5 Find the range of the ages (max minus min)
range_age=max_age-min_age
print(f'El rango de edad es de {range_age}')

# 6 Compare the value of (min - average) and (max - average), use abs() method (VALOR ABSOLUTO)
comp_min=abs(min_age-prom_ages)
comp_max=abs(max_age-prom_ages)
print('True' if comp_min==comp_max else 'False') # Comparo usando ternarios (muy util)

# 7 Find the middle country(ies) in the countries list
countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

middle_country_index=len(countries)//2
print(countries[middle_country_index])

# 8 Divide the countries list into two equal lists if it is even if not one more 
# country for the first half.
half_list_a=countries[0:middle_country_index+1]
print(half_list_a)
half_list_b=countries[middle_country_index+1:]
print(half_list_b)

# 9 Unpack the first three countries and the rest as scandic countries.
# El asterisco indica que todos los siguientes valores se asignan a una misma variable
# que va a ser una nueva lista.
countrie_a,countrie_b,countrie_c,*scandic_countries=countries 
print(countrie_a)
print(countrie_b)
print(countrie_c)
print(scandic_countries)