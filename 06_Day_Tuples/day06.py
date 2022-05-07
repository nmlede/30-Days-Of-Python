# Exercises: Level 1
# Create an empty tuple
tpl=tuple()
tpl=()

# Create a tuple containing names of your sisters and your brothers 
# (imaginary siblings are fine)
tpl_bro=('Matias','Simon')
tpl_sis=('Denisse','Virginia')
print(tpl_bro)
print(tpl_sis)
# Join brothers and sisters tuples and assign it to siblings
tpl_fam=tpl_bro+tpl_sis
print(tpl_fam)

# How many siblings do you have?
print(f'Cantidad de hermanos: {len(tpl_fam)}')

# Modify the siblings tuple and add the name of your father and mother 
# and assign it to family_members
lst_temp=list(tpl_fam) # Las tuplas no se pueden modificar, hay que castarlas a listas para editarlas
lst_temp.append('Karina')
family_members=tuple(lst_temp)
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
matias,simon,denisse,virginia,karina=family_members
print(matias,simon,denisse,virginia,karina)

# Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
tpl_fruits=('banana','manzana','pera')
tpl_veg=('morron','zapallo','cebolla')
tpl_ani=('perro','gato','ave')
food_stuff_tp=tpl_fruits+tpl_veg+tpl_ani
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or 
# food_stuff_lt list.
print(food_stuff_lt[0:(len(food_stuff_lt)//2)-1]+food_stuff_lt[len(food_stuff_lt)//2:])

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3]+food_stuff_lt[-3:])

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
