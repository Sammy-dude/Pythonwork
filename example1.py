from random import choice

print("Welcome to my new Program")
print("Select one of the values\n 1: Add \n 2: multipicaiton \n 3: Substrct \n 4: Divid")
def Add (x,y):
    return x+y
def Mul (x,y):
    return x*y
def Sub (x,y):
    return x-y
def Div (x,y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# for  i in range(1, 11):
#     print("aaa"*i)

choice=  input("enter your selection ")

num1= float(input("enter your first number "))

num2= float(input("enter your second number "))
if choice in ['1', '2', '3', '4']:

    if choice == "1":
        print(f'here is the result: {Add(num1,num2)}')
    elif choice == "2":
        print(f'here is the result: {Mul(num1,num2)}')
    elif choice == "3":
        print(f'here is the result: {Sub(num1,num2)}')
    elif choice == "4":
        print(f'here is the result: {Div(num1,num2)}')
else:
    print("Please enter a valid choice")

Total = (num1 + num2)

print ( f"here is the provided value  {Total}")
