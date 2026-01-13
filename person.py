# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Student(Person):
#     def __init__(self, name, age, id):
#         super().__init__(name, age)
#         self.id = id
# a = Student("John", 26, 18)
# print(a.name)
# print(a.age)
# print(a.id)

# class Vehicle:
#     def __init__(self,brend):
#         self.brend = brend
#     def mov(self):
#         print("Transport harakatlanmoqda")
# d = Vehicle("HD")
# d.mov()
#
# class Car(Vehicle):
#     def __init__(self,brend):
#         super().__init__(brend)
#     def mov(self):
#         print("Mashina yurmoqda")
# l = Car("HD")
# l.mov()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#
# class Manager(Employee):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus
#
#     def get_total_salary(self):
#         return self.salary + self.bonus
#
#
#
# manager = Manager("Ali", 5000, 3000)
# print(manager.get_total_salary())  # 6500

# class Animal:
#     def sound(self):
#         print("Animal ovoz chiqarmoqda")
#
# class Dog(Animal):
#     def sound(self):
#         print("It vovullayapti")
#
# class Cat(Animal):
#     def sound(self):
#         print("Mushuk miyovlayapti")
#
# dog = Dog()
# cat = Cat()
# dog.sound()
# cat.sound()

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Balans to‘ldirildi: {amount}")
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Yechib olindi: {amount}")
#         else:
#             print("Yetarli mablag‘ yo‘q")
#
#
# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#
#     def add_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         self.balance += interest
#         print(f"Foiz qo‘shildi: {interest}")
#
# acc = SavingsAccount("Vali", 1000, 5)
# acc.deposit(500)
# acc.add_interest()
# acc.withdraw(300)
# print("Yakuniy balans:", acc.balance)

# class User:
#     def __init__(self, username):
#         self.username = username
#
#     def login(self):
#         print("User tizimga kirdi")
#
# class Admin(User):
#     def login(self):
#         print("Admin tizimga kirdi")
#
# user = User("ali")
# admin = Admin("admin")
#
# user.login()
# admin.login()

# class Shape:
#     def area(self):
#         return 0
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# rect = Rectangle(5, 4)
# print(rect.area())

# class Device:
#     def __init__(self, brand):
#         self.brand = brand
#
# class Phone(Device):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model
#
# phone = Phone("Vivo", "V60")
# print(phone.brand)
# print(phone.model)

# class Teacher:
#     def __init__(self, name):
#         self.name = name
#
#     def teach(self):
#         print("Dars o‘tilmoqda")
#
# class MathTeacher(Teacher):
#     def teach(self):
#         print("Matematika darsi o‘tilmoqda")
#
# teacher = Teacher("Ali")
# math_teacher = MathTeacher("Vali")
#
# teacher.teach()
# math_teacher.teach()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount  # фоизда (%)

    def final_price(self):
        return self.price - (self.price * self.discount / 100)

product = DiscountedProduct("Noutbuk", 1000, 17)
print(product.final_price())  # 850
