#1. Print numbers from 1 to 10 using a for loop.
for number in range(1, 11):
	print(number)

#2. Print numbers from 10 to 1 using a while loop.

number = 10

while number >= 1:
    print(number)
    number -= 1
    
#3. Print the multiplication table of a number.

number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")
    
#4. Find the sum of numbers from 1 to n.
	
number = int(input("Enter n: "))

if number < 1:
    print("Enter a positive number")
else:
    total = 0
    for value in range(1, number + 1):
        total += value
    print(f"Sum: {total}")
    
#5. Find the factorial of a number.

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    for value in range(1, number + 1):
        factorial *= value
    print(f"Factorial: {factorial}")
	
#6. Print all even numbers between 1 and 100.

for number in range(2, 101, 2):
    print(number)
	
#7. Reverse a number using a loop.


number = int(input("Enter a number: "))
sign = 1 
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f"Reversed number: {sign * reversed_number}")

#8. Count the digits of a number.

number =int(input("Enter a number: "))
digits = 0

while number > 0:
    digits += 1
    number //= 10

print(f"Number of digits: {digits}")
	
#9. Check whether a number is prime.

number = int(input("Enter a number: "))
is_prime = number >= 2
divisor = 2

while divisor * divisor <= number and is_prime:
    if number % divisor == 0:
        is_prime = False
    divisor += 1

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
	
#10. Print Fibonacci series up to n terms.

terms = int(input("Enter the number of terms: "))

if terms < 0:
    print("Enter a non-negative number of terms")
else:
    first = 0
    second = 1
    for i in range(terms):
        print(first, end=" ")
        first, second = second, first + second
    print()


