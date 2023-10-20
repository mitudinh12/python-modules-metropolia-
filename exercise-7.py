import random
#6.1
def task_1():
    seasons = ("spring", "summer", "autumn", "winter")
    user_input = int(input("Which month do you want to check the corresponding season? (1-12)  "))
    if user_input in [12, 1, 2]:
        print(seasons[3])
    elif user_input in [3, 4, 5]:
        print(seasons[0])
    elif user_input in [6, 7, 8]:
        print(seasons[1])
    else:
        print(seasons[2])

#6.2
def task_2():
    names = set()
    name = input("Enter a name: ")
    while name != "":
        if name in names:
            print("Existing name")
        else:
            print("New name")
        names.add(name)
        name = input("Enter a name: ")

    for i in names:
        print(i, end='\n')


