#1. Check whether a number is positive, negative, or zero.

number = float(input("Enter a number: "))

if number > 0:
	print("Positive")
elif number < 0:
	print("Negative")
else:
	print("Zero")

#2. Check whether a person is eligible to vote.

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
#3. Find the largest of three numbers.

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if first >= second and first >= third:
    largest = first
elif second >= first and second >= third:
    largest = second
else:
    largest = third

print(f"Largest number: {largest}")

#4. Check whether a year is a leap year.

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
    
#5. Create a grade system based on marks.

marks = float(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 0:
    grade = "F"
else:
    grade = "Invalid marks"

print(f"Grade: {grade}")

#6. Check whether a number is divisible by 5 and 11.

number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("The number is divisible by both 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")
    
#7. Create a simple calculator using if-elif-else.

first = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second = float(input("Enter the second number: "))

if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
elif operator == "/":
    if second == 0:
        print("Cannot divide by zero")
    else:
        result = first / second
        print(f"Result: {result}")
else:
    print("Invalid operator")

if operator in ["+", "-", "*"]:
    print(f"Result: {result}")
