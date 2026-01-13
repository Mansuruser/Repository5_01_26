# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# 1
# class Person:
#     pass
# 2
# class Car:
#     pass
#
# car1 = Car()
# 3
# class Student:
#     def __init__(self):
#         self.name = ""
# s = Student()
# s.name = "Ali"

# 4
# class Dog:
#     def bark(self):
#         print("Woof")

# 5
# class Book:
#     def __init__(self, title):
#         self.title = title

# 6
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

# 7
# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
# l = Laptop("HP", 800)
# print(l.brand, l.price)

# 8
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

# 9
# class Teacher:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(self.name)

# 10
# class Animal:
#     def __init__(self, type):
#         self.type = type

# 11
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(self.name, self.age)

# 12
# class Car:
#     def start(self):
#         print("Mashina yondi")

# 13
# class BankAccount:
#     def __init__(self):
#         self.balance = 0

# 14
# class Phone:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
# p = Phone("Samsung", "A51")

# 15
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def show_marks(self):
#         print(self.marks)

# 16
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2

# 17
# class Employee:
#     def __init__(self, salary):
#         self.salary = salary
#
#     def show_salary(self):
#         print(self.salary)

# 18
# class Movie:
#     def __init__(self, title, year):
#         self.title = title
#         self.year = year
#
# m = Movie("Avatar", 2022)

# 19
# class Account:
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount

# 20
# class House:
#     def __init__(self, rooms):
#         self.rooms = rooms
#
# h = House(4)
# print(h.rooms)


# 21
# class Person:
#     pass
#
# p = Person()
# p.name = "Ali"
# print(p.name)

# 22
# class Car:
#     def __init__(self, color):
#         self.color = color
#
# c1 = Car("Red")
# c2 = Car("Blue")
# print(c1.color, c2.color)

# 23 (self yo‘q — xato)
# class Student:
#     def show():
#         print("Hello")

# Student().show()  ❌ TypeError

# 24
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def withdraw(self, amount):
#         self.balance -= amount

# 25
# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def info(self):
#         print(self.brand, self.price)

# 26
# class User:
#     def __init__(self, password):
#         self.password = password
#
#     def check(self, pwd):
#         return self.password == pwd

# 27
# class Car:
#     count = 0
#
#     def __init__(self):
#         Car.count += 1

# 28
# class Person:
#     def __init__(self):
#         print("Yangi obyekt yaratildi")

# 29
# class Student:
#     def __init__(self, subjects):
#         self.subjects = subjects

# 30
# class Student:
#     def __init__(self, name):
#         self.name = name
#
# class School:
#     def __init__(self, student):
#         self.student = student
#
# s = Student("Ali")
# school = School(s)
# print(school.student.name)