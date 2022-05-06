# Exercises: Day 5

# Exercises: Level 1
# 1 Declare an empty list
from __future__ import print_function
import re
from signal import ITIMER_REAL
from types import coroutine
from xml.sax.handler import property_interning_dict

from numpy import irr, sort


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
print(sort(it_companies)) # Ordena alfabeticamente.

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

# Remove the first IT company from the list

# Remove the middle IT company or companies from the list

# Remove the last IT company from the list

# Remove all IT companies from the list

# Destroy the IT companies list

# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.