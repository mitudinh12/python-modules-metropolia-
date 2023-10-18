import math
import random

#Exercise 2.1
def program_1():
    name_input = input("What is your name? ")
    print(f"Hello, {name_input}")

#Exercise 2.2
def program_2():
    radius = float(input("Provide radius value: "))
    area = math.pi*radius**2
    print(area)

#exercise 2.3
def program_3():
    length = float(input("Please provide length of rectangle: "))
    width = float(input("Please provide width of rectangle: "))
    perimeter = (length + width) * 2
    area = length * width
    print(f"The perimeter of the rectangle is {perimeter} and the area of it is {area}")

#exercise 2.4
def program_4():
    integer_1 = int(input("Provide integer 1: "))
    integer_2 = int(input("Provide integer 2: "))
    integer_3 = int(input("Provide integer 3: "))
    sum = integer_1 + integer_2 + integer_3
    product = integer_1 * integer_2 * integer_3
    average = sum / 3
    print(f"Sum is {sum}")
    print(f"Product is {product}")
    print(f"Average is {average}")

#exercise 2.6
def program_6():
    random_three = []
    i = 0
    while i < 3:
        random_number = random.randint(0,9)
        random_three.append(random_number)
        i += 1
    print(random_three)

    random_four = []
    i = 0
    while i < 4:
        random_number = random.randint(1,6)
        random_four.append(random_number)
        i += 1
    print(random_four)

