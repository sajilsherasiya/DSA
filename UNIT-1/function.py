# 1. Hello World
def hello_world():
    return "Hello, World!"

print("1.", hello_world())


# 2. Greeting
def greet(name):
    return "Hello, " + name

print("2.", greet("Rahul"))


# 3. Add two numbers
def add(a, b):
    return a + b

print("3.", add(10, 20))


# 4. Square
def square(n):
    return n * n

print("4.", square(5))


# 5. Even or Odd
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print("5.", even_or_odd(7))


# 6. Maximum of two numbers
def maximum_two(a, b):
    return max(a, b)

print("6.", maximum_two(10, 20))


# 7. Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print("7.", celsius_to_fahrenheit(25))


# 8. Area of circle
def circle_area(radius):
    pi = 3.14159
    return pi * radius * radius

print("8.", circle_area(5))


# 9. Factorial
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print("9.", factorial(5))


# 10. Positive, Negative or Zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print("10.", check_number(-10))


# 11. Maximum of three numbers
def maximum_three(a, b, c):
    return max(a, b, c)

print("11.", maximum_three(10, 30, 20))


# 12. Count vowels
def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count

print("12.", count_vowels("Hello World"))


# 13. Reverse string
def reverse_string(text):
    return text[::-1]

print("13.", reverse_string("Python"))


# 14. Palindrome
def is_palindrome(text):
    return text.lower() == text.lower()[::-1]

print("14.", is_palindrome("madam"))


# 15. Sum of list
def list_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print("15.", list_sum([10, 20, 30, 40]))


# 16. Largest element
def largest_element(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

print("16.", largest_element([10, 50, 30, 20]))


# 17. Remove duplicates
def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

print("17.", remove_duplicates([1, 2, 2, 3, 3, 4]))


# 18. Count element
def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1

    return count

print("18.", count_element([1, 2, 2, 3, 2, 4], 2))


# 19. Prime number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print("19.", is_prime(17))


# 20. Prime numbers between two numbers
def primes_between(start, end):
    primes = []

    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)

    return primes

print("20.", primes_between(10, 30))


# 21. Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

print("21.", fibonacci(10))


# 22. Second largest
def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]


numbers = [10, 50, 30, 40, 20]

print("22.Second largest:", second_largest(numbers))

# 23. Sort without sort()
def my_sort(numbers):
    numbers = numbers.copy()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

print("23.", my_sort([50, 20, 40, 10, 30]))


# 24. Merge two lists and remove duplicates
def merge_lists(list1, list2):
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result

print("24.", merge_lists([1, 2, 3], [3, 4, 5]))
