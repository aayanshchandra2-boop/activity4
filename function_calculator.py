a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
operation=input("Enter the operation (multiply, subtract, divide, add): ")

if operation=="multiply":
    result=a*b
    print("The result of multiplication is:",result)
    if operation=="subtract":
        result=a-b
        print("The result of subtraction is:",result)
        if operation=="divide":
            if b!=0:
                result=a/b
                print("The result of division is:",result)
                if operation=="add":
                    result=a+b
                    print("The result of addition is:",result)
            else:
                print("Error: Division by zero is not allowed.")


