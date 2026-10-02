# Вопрос 1

# Изменяемые это те контейнеры которые можно изменить после создание, а не изменяемых нет.
# пример: лист - его можно изменить после создание, а кортеж нет но можно его сделать листом изменить и вернуть кортеж.



# Вопрос 2

# Лист - это контейнер имеющий методы и он изменяемый в отличие от кортежа, Кортеж используется там где нужно создать что-то один раз.

# Вопрос 3

# Try, except и finallly помогают запустить код даже если в нем имеется ошибки, 
# Try - это попытка запуска кода зная что есть ошибка
# Except - это определение того ошибки которое может случится, и  не отключится если будет ошибка.
# Finally - это то что будет работать не зависимо от Try и Except.

# Вопрос 4

# Переиенные - это то что мы даем значение для использование его в коде.
# int - (Integer) это переменное которое принимает число.
# float - тоже принимает числло но в десятичном виде.
# str - (String) это переменное которое принимает буквы.
# bool - это переменное которое возвращает правду или ложь (True, False)


# Вопрос 5 

# def fibonacci(n):
#     r = []
#     a = 1
#     b = 1
#     for _ in range(n):
#        r.append(a)
#        a, b = b, a + b
#     return r

# print(fibonacci(5))




# Question 6

# lict = [i for i in range(1, 51) if i % 2 == 0 and i % 3 == 0]

# print(lict)


# question 7

# with open("text.txt", "r")as file:
#     a = file.readlines()
#     for i in a:
#         b = len(a) 
#     print(b)

# 8

# def word_count(text):
#     text = input().split()
#     a = {
#         "text": text.count
#     }
#     return a

# c =input()
# print(word_count(c))


# 9

# class BancAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         return f"Deposit: {amount}, balance: {self.balance}"

#     def withdraw(self, amount):
#         if amount > 0 and amount < self.balance:
#             self.balance -= amount
#         else:
#             print("Недостаточнр средств")
#         return f"Withdraw: {amount}, balance: {self.balance}"
       
    

#     def __str__(self):
#         return f"Owner: {self.owner}, balance: {self.balance}"

# a = BancAccount("Abdurahmon", 1500)

# print(a.deposit(500))
# print(a.withdraw(300))
# print(a)


# 11
# with open("file.txt", "r") as file:
#     a = file.readlines

# def process_grades(file):
#     for i in file: