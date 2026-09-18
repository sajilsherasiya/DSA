def operation(a,b):
    return a+b,a-b,a*b,a/b
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print(f"Addition: {operation(x,y)[0]}")
print(f"Subtraction: {operation(x,y)[1]}")  
print(f"Multiplication: {operation(x,y)[2]}")
print(f"Division: {operation(x,y)[3]}")