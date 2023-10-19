import random

#4.1
def task_1():
    i = 0
    while i in range(1000):
        if i % 3 == 0:
            print(i)
            i+= 1
        i+= 1

#4.2
def task_2():
    inches_input = float(input("Please provide value in inches: "))
    while inches_input >= 0:
        cm_conversion = inches_input * 2.54
        print(f"The centimeter value is {cm_conversion}")
        inches_input = float(input("Please provide value in inches: "))

#4.3
def task_3():
    numbers = []
    number = input("Give a number: ")
    while number != "":
        numbers.append(int(number))
        number = input("Give a number: ")
    organized_numbers = sorted(numbers)
    print(f"Smallest number is {organized_numbers[0]} and biggest number is {organized_numbers[-1]}")

#4.4
def task_4():
    number = random.randint(1,10)
    guess = int(input("Guess the number: "))
    while guess != number:
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        guess = int(input("Guess the number: "))
    print("Correct")

#4.5
def task_5():
    username = "mitudinh"
    password = "badminton123"
    username_input = input("Username: ")
    password_input = input("Password: ")

    i = 0
    while username_input != username or password_input != password:
        username_input = input("Username: ")
        password_input = input("Password: ")
        i += 1
        if i == 4:
            print("Access denied")
            break

    if username_input == username and password_input == password:
        print("Welcome")







