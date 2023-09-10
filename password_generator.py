#Password Generator Project
import random
Characters_all="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"
while True:
    length=int(input("Enter the length of password:"))
    no_of_times=int(input("Enter the number of times you want generate password:"))
    for i in range(0,no_of_times):
        password=""
        for j in range(0,length):
            pas=random.choice(Characters_all)
            password=password+pas
        print("Generated password:",password)
    repeat=input("Are you want to generate password again yes or no:")
    if repeat=="NO" or repeat=="no":
        break
print("Thank you!")

