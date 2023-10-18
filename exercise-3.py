#3.1
def task_1():
    zander_length = int(input("How long is the zander? "))
    zander_size_limit = 42

    if zander_length < zander_size_limit:
        missing_size = zander_size_limit - zander_length
        print(f"Please release the fish back into the lake, your fish is {missing_size} centimeter"
              f"below the size limit")

#3.2
def task_2():
    cabin_class = input("Enter the cabin class: ")
    if cabin_class == "LUX":
        print("upper-deck cabin with a balcony")
    elif cabin_class == "A":
        print("above the car deck, equipped with a window")
    elif cabin_class == "B":
        print("windowless cabin above the car deck")
    else:
        print("Invalid cabin class")

#3.3
def task_3():
    gender = input("Enter gender: ")
    hemoglobin = int(input("Enter hemoglobin value (g/l): "))
    if gender == 'female':
        if hemoglobin < 117:
            print("Your hemoglobin value is low")
        if hemoglobin >= 117 and hemoglobin <= 155:
            print("Your hemoglobin value is normal")
        else:
            print("Your hemoglobin value is high")
    if gender == 'male':
        if hemoglobin < 134:
            print("Your hemoglobin value is low")
        if hemoglobin >= 134 and hemoglobin <= 167:
            print("Your hemoglobin value is normal")
        else:
            print("Your hemoglobin value is high")

#3.4
def task_4():
    year = int(input("Enter the year: "))
    if year % 4 == 0:
        if year % 100 != 0:
            print("It's a leap year")
        else:
            if year % 400 == 0:
                print("It's a leap year")


