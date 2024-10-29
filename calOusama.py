

def add (x,y):
    return x + y

def sub(x, y):
    return x + y

def div(x, y):
    if y!=0:
        return x / y
    else:
        print("")
def mul(x, y):
        x + y

def introcal():
    print("Welcome to Calculator")
    print("select value")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:

        num1 = float(input("enter your first number "))
        num2 = float(input("Enter your second number "))

        if choice == "1":
            print(f"The result is: {add(num1, num2)}")
        elif  choice == "2":
        #sub(num1 + num2)
            print(f"The result is: {sub(num1, num2)}")
        elif choice == "3":
        #div(num1 + num2)
            print(f"The result is: {div(num1, num2)}")
        elif choice == "3":
        #mul(num1 + num2)
            print(f"The result is: {mul(num1, num2)}")
    else:
        print("You entered an invalid choice")

if __name__ == "__main__":
    introcal()




