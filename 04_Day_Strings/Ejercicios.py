#1
thirty = 'Thirty '
days = 'Days '
of = 'Of '
python = 'Python'
str1 = thirty+days+of+python
print(str1)

#3, 4, 5, 6, 7, 8, 9, 10, 11, 13
company = 'Coding For All'
print(company,len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.find('Coding'))
print(company.index('Coding'))
print('Coding' in company)
print(company.replace('Coding','Python'))
print(company.split(' '))

#14
str2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str2.split(', '))

#15, 16, 17
print(company[0])
print(company[len(company)-1])
print(company.rindex('l'))
print(company[10])

#18, 19, 20, 21
acronimo_pfe = 'PFE'
acronimo_cfa = 'CFA'
print(acronimo_cfa.index('C'))
print(acronimo_cfa.index('F'))

#22
str3 = 'Coding For All People'
print(str3.rindex('l'))

#23, 24
str4 = 'You cannot end a sentence with because because because is a conjunction'
print(str4.index('because'))
print(str4.rindex('because'))