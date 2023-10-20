import random
#6.1
def task_1():
    while True:
        dice_result = random.randint(1,6)
        print(dice_result)
        if dice_result == 6:
            break

#6.2
def task_2(sides):
    while True:
        dice_result = random.randint(1,sides)
        print(dice_result)
        if dice_result == sides:
            break

#6.3
def conversion(gallon):
    litres = gallon * 0.264172
    return litres
def main_program_task_3():
    gallon = input("Volume of gasoline in gallon: ")
    while gallon != "":
        print(conversion(float(gallon)))
        gallon = input("Volume of gasoline in gallon: ")

#6.4
def sum(integers):
    sum_integers = 0
    for integer in integers:
        sum_integers += integer
    return sum_integers
def main_program_task_4():
    integer_list = [1,2,3,4,9,8,7,6]
    print(sum(integer_list))

#6.5
def even_list_conversion(number_list):
    even_list = []
    for i in number_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
def main_program_task_5():
    test_list = [6,4,5,6,9,7,4,2,5,7]
    print(test_list)
    print(even_list_conversion(test_list))

#6.6
def value_calculation(diameter_centimeter, price):
    diameter_meter = diameter_centimeter * 0.01
    value = price / diameter_meter
    return value
def main_program_task_6():
    pizza_1_diameter = int(input("Diameter of pizza 1 in cm: "))
    pizza_1_price = int(input("Price of pizza 1: "))
    pizza_2_diameter = int(input("Diameter of pizza 2 in cm: "))
    pizza_2_price = int(input("Price of pizza 2: "))
    if value_calculation(pizza_1_diameter, pizza_1_price) > value_calculation(pizza_2_diameter, pizza_2_price):
        print("Pizza 1 has better value")
    else:
        print("Pizza 2 has better value")

