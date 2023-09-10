#Calculator Project
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd Number:"))
choice=int(input("Enter operator :\n 1 for Addition:\n 2 for Subtration:\n 3 for Multiplication:\n 4 for Division:\n"))
if(choice==1):
    print("Addition of two number is:",n1+n2)
elif(choice==2):
    print("Subtration of two number is:",n1-n2)
elif(choice==3):
    print("Multiplication of two number is:",n1*n2)
elif(choice==4):
    print("Division of two number is:",n1/n2)
else:
    print("Its a invalid operator:\nPlease Enter number in between 1 to 4 ")
