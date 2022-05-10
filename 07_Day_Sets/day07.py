# Exercises: Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter') # add para agregar un elemento al principio
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_agregadas={'Tsoft','Nokia'} # Nuevo conjunto con elementos
it_companies.update(it_agregadas) # update para agregar varios elementos (actualizando conjuntos)
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Join A and B
C=A.union(B) # union para unir conjuntos
D=A
D.update(B) # update para actualizar A con los valores de B
print(C)
print(D)

# Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B))

# Is A subset of B
print(B.issubset(A))
print(B.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))
print(B.isdisjoint(A))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A
del B

# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set=set(age) # Convertir lista a conjunto remueve los duplicados y ordena ascendentemente
print(age)
print(len(age))
print(age_set)
print(len(age_set))

string='I am a teacher and I love to inspire and teach people'
#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
string_split=string.split(' ')
unique_words=set(string_split)
print(f'La cantidad de palabras unicas es: {len(unique_words)}, y son: {unique_words}')