# def silnia(n):
#     if n==1:
#         return 1
#     return n * silnia(n-1)
# print(silnia(9))
import itertools
# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo(n-2)
# print(fibo(-10))

# while True:
#     try:
#         n1 = int(input('Liczba 1: '))
#         n2 = int(input('Liczba 2: '))
#         sum = n1 + n2
#         print(f'Suma to: {sum}')
#         break
#     except ValueError:
#         print('Wprowadz liczbe')

# a = [2, 5, 9]
# try:
#     print(a[3])
# except IndexError:
#     pass

# a = "abcdefghijk"
# try:
#     msg = a + 5
# except BaseException:
#     msg = "Nie możesz dodać int do str"
# print(msg)

# list = [5, 10, 20]
# try:
#     msg = list[5]
# except IndexError:
#     msg = "Jesteś poza zakresem listy"
# print(msg)

# def dzielenie(a, b):
#     try:
#         wynik = a / b
#     except ZeroDivisionError:
#        wynik = "Nie dziel przez 0"
#     finally:
#         print(wynik)
#
# dzielenie(4, 8)

# fo = open("text.txt", "r", encoding="utf-8")
# print("Nazwa pliku: ", fo.name)
#
# line = fo.readline()
# print("czytaj linie: >" + line + "<")
# fo.seek(0)
# line = fo.readline()
# print("czytaj linie: >" + "<")
# pos = fo.tell()
# print('aktualna pozycja: >' + str(pos) '<')
# fo.close()

# import os
# os.mkdir('00_abc')
# os.system('dir')

# from time import sleep
# print('dobranoc')
# sleep(2)
# print('dzien dobry')

# import fruit
# fruit.lemon(303)

    # from fruit import lemon
    # lemon(303)

# o = open('text.txt', 'r', encoding='utf-8')
# full = o.read()
# print(full)

# with open('text.txt', 'w') as file:
#     file.write(('hello world'))



# with open('text.txt', 'r', encoding='utf-8') as file:
#     content_list = file.readlines()[1]
#     print(content_list)

# with open('text2.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text)

# def cb_readlines(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         content_array = []
#         for line in file:
#             content_array.append(line.replace('\n', ''))
#     return content_array
# print(cb_readlines(filename='text2.txt'))

# from itertools import islice
# def slice_file(file_path, n):
#     with open(file_path, encoding='utf-8') as myFile:
#         content_array = []
#         for line in islice(myFile, n):
#             content_array.append(line.replace('\n', ''))
#         return content_array
# print(slice_file('text2.txt', 3))

# def longest_word(str1):
#     with open(str1, encoding='utf-8') as file:
#         file_read = file.read().split()
#     longest = ''
#     for word in file_read:
#         if len(word) > len(longest):
#             longest = word
#     return longest
# print(longest_word('text2.txt'))

# def count_lines(fileName):
#     with open(fileName) as file:
#         counter = 0
#         for line in file:
#             counter += 1
#         return counter
# print(count_lines('text2.txt'))

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# def save_list(fileName, lst):
#     with open(fileName, 'w', encoding='utf-8') as file:
#         for el in lst:
#             file.write(str(el) + '\n')
# save_list('txt2.txt, color')

# with open('abc.txt', 'a') as myfile:
#     myfile.write("Ćwiczenia z Pythona\n")
# with open('abc.txt', 'r') as myfile:
#     print(myfile.read())

# import os
# statinfo = os.stat('text.txt')
# print("Statystyka zwykłego pliku: ", statinfo)

# import shutil
# shutil.copyfile('text.txt', 'text2.txt')

# from math import sin
# print(sin(1/2))

temperatury = [
    37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
    35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
    39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
    36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
    33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
    39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
    34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
    34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
    34.2, 40.2, 34.3, 35.3
]
# wynik = list(filter(lambda x: x >=40.0, temperatury))
# print(wynik)
# wynik_sorted = sorted(wynik)
# print(wynik_sorted)

# print(temperatury)
# sum1 = 0
# for temp in temperatury:
#     sum1 += temp
# sr = sum1/len(temperatury)
# print(sr)

# from statistics import mean
# sr_temp = mean(temperatury)
# odch = list(map(lambda x: round(x - sr_temp,2), temperatury))
# print(odch)

# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# print(reduce(lambda a, b: a + b, nums))

# szecsciany = [x**3 for x in range(20)]
# print(szecsciany)

# pusta = lambda a: a
# print(pusta)

# x = lambda a: a+15
# print(x(16))

# z = lambda x, y: x * y
# print(z(5, 9))

# subject_marks = [('Język angielski', 88),
#                  ('Nauka',           90),
#                  ('Matematyka',      97),
#                  ('Nauki społeczne', 82)]
# print('Oryginalna lista krotek: ')
# print(subject_marks)
# subject_marks.sort(key=lambda x: x[1])
# print('\nSortowanie listy krotek: ')
# print(subject_marks)

# models = [{'marka': 'Nokia',   'model': '3310',   'kolor': 'Czarny'},
#           {'marka': 'Apple',   'model': '11',     'kolor': 'Złoty'},
#           {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]
#
# print('\norygnalna lista słowników: ')
# print(models)
# models.sort(key=lambda x: x['kolor'])
# print('\nposortowana lista słowników: ')
# print(models)

# starts_with = lambda str1: str1.upper().startswith('P')
# print(starts_with('python'))

# import datetime
# now = datetime.datetime.now()
# print(now)
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# t = lambda x: x.time()
# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))

# is_num = lambda q: q.replace('.', '', 1).isdigit()
# print(is_num('26587'))
# print(is_num('4.2365'))
# print(is_num('-12547'))
# print(is_num('00'))
# print(is_num('A001'))
# print(is_num('001'))
# print("\nWydrukuj liczby kontrolne:")
# is_num1 = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)
# print(is_num1('-16.4'))
# print(is_num1('-24587.11'))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('Oryginalna lista: ')
# print(nums)
# print('\nPrzyste liczby z listy: ')
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)
# print('\nNieparzyste liczby: ')
# odd_nums = list(filter(lambda x: x % 2 != 0, nums))
# print(odd_nums)

# array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array_nums2 = [1, 2, 4, 8, 9]
# print("Oryginalne tablice:")
# print(array_nums1)
# print(array_nums2)
# result = list(filter(lambda x: x in array_nums1, array_nums2))
# print('\nPrzeciecie tablic: ', result)

# weekdays = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
# days = filter(lambda day: len(day) == 6, weekdays)
# for d in days:
#     print(d)

# nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, nums))
# print(result)

# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa", "kobyłamamałybok"]
# Palindroms = list(filter(lambda x: x == x[::-1], texts))
# print(Palindroms)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square = [x**2 for x in nums if x % 2 ==0]
# cube = [x**3 for x in nums]
# print(square)
# print(cube)

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums3 = map(lambda x, y: x + y, nums1, nums2)
# print(list(nums3))

# nums = [2, 4, 6, 9, 11]
# n = 5
# a = list(map(lambda x: x*n, nums))
# print(a)

# nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
# x = abs(sum([num for num in nums if num <0]))
# print(x)


# klasy w programowaniu obiektowym Python:

# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)

# class Parrot:
#
#     species = 'papuga'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
#
# print(blu.name, "ma", blu.age, "lat")
# print(woo.name, "ma", woo.age, "lat")


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfunc(self):
#         print("Cześć, mam na imię " + self.name)
#
# Me = Person('Kris', 34)
# print(Me.name)
# print(Me.age)
# Me.myfunc()

#
# class Account:
#     def __init__(self, name, status = 0):
#         self.name = name
#         self.status = status
#
#     def info(self):
#         print('name: ', self.name)
#         print('status: ', self.status)
#
#     def withdraw(self, amount):
#         self.status -= amount
#
#     def deposit(self, amount):
#         self.status += amount
#
# jk = Account('Krzysiek P', 2000)
# jk.info()
# jk.deposit(2500)
# jk.info()
# jk.withdraw(3000)
# jk.info()
# jk.status = 0
# jk.info()


# class MyClass:
#      x = 5
# p1 = MyClass()
# print(p1.x)

# class Jets:
#
#     def __init__(self, name, origin):
#         self.name = name
#         self.origin = origin
#
# first_item = Jets("Boeing 747", "US")
# print(first_item.name)

# class Jets:
#
#     def __init__(self, name, origin):
#         self.name = name
#         self.origin = origin
#
#
# first_item = Jets("Boeing 747", "US")
#
# a = first_item.name
# print(a)

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# modelX = Vehicle(240, 18000)
# print(modelX.max_speed, modelX.mileage)

# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#
# RedCar = Car('Red', 30_000)
# BlueCar = Car('Blue', 20_000)
# print(BlueCar.color, 'samochod ma', BlueCar.mileage, 'kilometrów przebiegu.')
# print(RedCar.color, 'samochod ma', RedCar.mileage, 'kilometrów przebiegu.')


# class Jets:
#     def __init__(self, name, origin, quantity):
#         self.name = name
#         self.origin = origin
#         self.quantity = quantity
#
# first_item = Jets("Boeing 747", "US", 87)
# second_item = Jets("Airbus A380", "FU", 35)
# third_item = Jets("Embraer 195", "BR", 0)
#
# list = []
# for jet in (first_item, second_item, third_item):
#     list.append(jet.name)
#     list.append(jet.origin)
#     list.append(jet.quantity)
# print(list)

# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#
# np2005=Nobel("Peace", 2005, "Muhammad Yunus")
# print(np2005.category, np2005.year, np2005.winner)

# class Rectangle():
#     def __init__(self, l, w):
#         self.length = l
#         self.width  = w
#
#     def rectangle_area(self):
#         return self.length*self.width
#
# newRectangle = Rectangle(12, 10)
#
# print(newRectangle.rectangle_area())


import math
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def circle_area(self):
#         return 2 * math.pi * self.r ** 2
#
#     def circle_round(self):
#         return 4 * math.pi * self.r
#
# newCircle = Circle(6)
# print(newCircle.circle_area())
# print(newCircle.circle_round())

# class Temp:
#     def convert_Fahrenheit(self, C):
#         return (C*(9/5))+32
#     def convert_Celsius(self, F):
#         return (F-32)*(5/9)
#
# C_con = Temp().convert_Fahrenheit(25)
# print(C_con)

# class Student():
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#         self.age = "undefined"
#         self.marks = "undefined"
#     def display(self):
#         print(self.name)
#         print(self.roll)
#         print(self.age)
#         print(self.marks)
#     def set_age(self, age):
#         self.age = age
#     def set_marks(self, marks):
#         self.marks = marks
#
# student1 = Student('Jan Kowalski', 11)
# student1.display()
# student1.set_age(25)
# student1.set_marks(4)
# student1.display()

# class Osoba:
#     def __init__(self, imie, nazwisko, wiek):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.wiek = wiek
#
#     def pelne_imie(self):
#         return self.imie + ' ' + self.nazwisko
#
# JK = Osoba('Jan', 'Kowalski', 33 )
# print(JK.pelne_imie())