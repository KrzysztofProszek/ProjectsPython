# tuple1 = (10, 20, 30, 40, 50)
# tuple2 = tuple1[::-1]
# print(tuple2)

# list = ["Emma Margaryan",
# "Anna Góralik",
# "Patryk Kotański",
# "Karol Grella",
# "Dymitr Garafowski",
# "Barabara Cygal",
# "Aleksandra Kurdel - Lizer",
# # "Jan Sokołowski",
# "Grzegorz Kossakowski", ]
# list2=sorted(list)
# list3=len(list2)
# print(list3)

# keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
# values = [10, 20, 30]
# dictionary =zip(keys, values)
# slownik = dict(dictionary)
# print(slownik)

# sample_set = {"Żółty", "Pomarańczowy", "Czarny"}
# sample_list = ["Niebieski", "Zielony", "Czerwony"]
# sample_set.update(sample_list)
# print(sample_set)

# string = 'Python'
# for litera in string:
#     print('litera:', litera)
#
# print("Przykład range() w Pythonie")
# print("Uzyskaj liczby z zakresu od 0 do 5")
# for i in range(6):
#     print(i)

# a = input("Podaj liczbe: ")
# b = input("Podaj liczbe: ")
# iloraz = float(a)/float(b)
# modulo = float(a)%float(b)
# calkowite = float(a)//float(b)
# print(iloraz, modulo, calkowite)

# x=1
# y=15
# if x>3 or y%2==0:
#     print('co najmniej jeden z warunkow spelniony')
#
# if x<=3 and y%2!=0:
#     print('Żaden warunek nie jest spełniony')
#
# keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
# values = [10, 20, 30]
# dict = dict()
# for i in range(len(keys)):
#     dict.update({keys[i]: values[i]})
# print(dict)

# a = int(input('podaj liczbe a: '))
# b = int(input('podaj liczbe b: '))
# division = 1
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         division = i
# print(division)

# a = int(input('Podaj liczbe: '))
# sum = 0
# for i in range(a+1):
#     sum += i
# print(sum)

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)

# def chain_lenght(str1):
#     x = 0
#     for item in str1:
#         x += 1
#     return x
#
# print(chain_lenght(input("wpisz znak: ")))

# def sum_elements(list1):
#     counter = 0
#     for i in list1:
#         counter += i
#     return i
# print(sum_elements([1, 2, 3, -7]))

# def multiple_elements(myList):
#     myMultiplication = 1
#     for i in myList:
#         myMultiplication *= i
#     return myMultiplication
# print(multiple_elements([1,2,3,4,5,6]))

# def highest_number(myList2):
#     max_value = myList2[0]
#     for i in myList2[1:]:
#         if i > max_value:
#             max_value = i
#     return max_value
# print(highest_number([1, 10, 20, 99]))


# charToCount = 'google.com'
# def countChar(argChar):
#     slownik = {}
#     for i in argChar:
#         keys = slownik.keys()
#         if i in keys:
#             slownik[i] += 1
#         else:
#             slownik[i] = 1
#     return slownik
# print(countChar(charToCount))


# def count_strings(lista1):
#     x = 0
#     for i in lista1:
#         if len(i) >= 2 and i[0] == i[-1]:
#             x += 1
#     return x
# print(count_strings(['abc', 'xyz', 'aba', '1221']))

# def chainCount(chain1):
#     if len(chain1) < 2:
#         return ""
#     a = chain1[0:2] + chain1[-2:]
#     return a
# print(chainCount("Python"))

