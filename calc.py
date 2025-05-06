import math
def sqrtof(n):
    return math.sqrt(n)
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"
def modulus(x, y): return x % y
def power(x, y): return x ** y

print("1.Add  2.Subtract  3.Multiply  4.Divide  5.Modulus  6.Power")
choice = input("Enter choice (1/2/3/4/5/6): ")
if choice == 7:
    n = int(input(" Enter the number "))
    print("the sqrt of the number is : ",sqrtof(n))
else:
    a = float(input("First number: "))
    b = float(input("Second number: "))

    if choice == '1': print("Result:", add(a, b))
    elif choice == '2': print("Result:", subtract(a, b))
    elif choice == '3': print("Result:", multiply(a, b))
    elif choice == '4': print("Result:", divide(a, b))
    elif choice == '5': print("Result:", modulus(a, b))
    elif choice == '6': print("Result:", power(a, b))
    else: print("Invalid input")