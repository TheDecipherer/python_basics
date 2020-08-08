# F to C converter

factor = 9 / 5
celsius = float(input('Enter the temperature in Celsius '))
fahrenheit = float((celsius * factor) + 32)
print('The temperature in Fahrenheit is {}'.format(str(fahrenheit)))

# Swap numbers

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
temp = a
a = b
b = temp
print('a and b are {}, {}'.format(str(a), str(b)))

# Name length problem

name = input('Enter your name: ')
length = len(name)
if length > 7:
    print(name)
elif length > 4 & length < 6:
    age = int(input('Enter your age: '))
    print(str(age))

# Calculator

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
operator = input('Enter the operation: ')
if operator == '+':
    print(str(a + b))
elif operator == '-':
    print(str(a - b))
elif operator == '*':
    print(str(a * b))
elif operator == '/':
    print(str(a / b))
else:
    print(str(a % b))


# Interest calculator

def calculator(input_pay):
    built_in_interest = 0
    if 20000 < input_pay < 50000:
        built_in_interest = 10
    elif 50000 < input_pay < 100000:
        built_in_interest = 20
    elif input_pay > 100000:
        built_in_interest = 30
    return built_in_interest


salary = int(input('Enter your salary: '))
if salary < 0:
    salary = int(input('Please enter a positive number: '))
interest = float(calculator(salary))
print('Your income tax is {}'.format(str(interest * salary / 100)))

# Factorial

number = int(input('Enter the number: '))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print('The factorial is {}'.format(str(factorial)))


# Password problem

def password_checker(input_password):
    input_length = len(input_password)
    if input_length > 6 and type(int(input_password[input_length - 1])):
        print('Access Granted')
    else:
        input_password = input('Enter a valid password')
        password_checker(input_password)


password = input('Please enter a password: ')
password_checker(password)

# FizzBuzz

user_input = input('Enter the numbers: ')
number_list = user_input.split(', ')
for i in range(0, len(number_list)):
    if int(number_list[i]) % 3 == 0 and int(number_list[i]) % 5 == 0:
        print('FizzBuzz')
    elif int(number_list[i]) % 3 != 0 and int(number_list[i]) % 5 != 0:
        print(str(int(number_list[i])))
    else:
        if int(number_list[i]) % 3 == 0:
            print('Fizz')
        else:
            print('Buzz')

# Address book

names = input('Enter the names: ').split(', ')
numbers = input('Enter the phone numbers: ').split(', ')

address_book = dict(zip(names, numbers))

user = input('Enter the user name: ')
print(address_book[user])
