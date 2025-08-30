def performop(choice):
 match choice:
    case 1:
           return num1+num2
    case 2:
           return   num1-num2
    case 3:
           return num1*num2
    case 4:
           return num1/num2
    case 5:
           return num1**num2
    case 6:
           return num1//num2
    case _:
           return "Enter valid operation to perform"
 
num1=float(input("Enter 1 st number:"))
num2=float(input("Enter 2 nd number:"))
print("1.Addition")
print("2.subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponential")
print("6.Floor Division")
choice=int(input("Enter a valid choice from the above i.e,1-6:"))
li=["+","-","*","/","**","//"]
res=performop(choice)
print('A',li[choice-1],'B=',res)
