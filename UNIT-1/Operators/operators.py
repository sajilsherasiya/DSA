#1. Perform addition, subtraction, multiplication, and division.

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print(f"Addition: {x+y}")
print(f"Subtraction: {x-y}")  
print(f"Multiplication: {x*y}")
print(f"Division: {x/y}")

#2. Find the remainder and quotient of two numbers.

diviser=int(input("Enter diviser: "))
divedent=int(input("Enter divedent: "))
print(f"Quotient is {divedent//diviser} and reminder is {divedent%diviser}")


#3. Check whether a number is even or odd.

x=int(input("Enter a number: "))
if x%2==0:
    print(f"{x} is even number")
else:
    print(f"{x} is odd number")
    
#4. Compare two numbers using relational operators.

x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
if x==y:
    print('both are equal')
else:
    print('not equal')
    
#5. Demonstrate logical operators (and, or, not).

has_id = True
is_adult = True
has_ticket = False

print("and:", has_id and is_adult)
print("or:", has_ticket or has_id)
print("not:", not has_ticket)

if has_id and is_adult:
	print("The person can enter.")

if has_ticket or has_id:
	print("At least one requirement is satisfied.")

if not has_ticket:
	print("The person does not have a ticket.")

#6. Demonstrate assignment operators (+=, -=, *=, /=).

a=int(input("enter value of a:"))
a+=1
print(f"+=:{a}")
a-=1
print(f"-=:{a}")
a*=a
print(f"*=:{a}")
a/=2
print(f"/=:{a}")

#7. Find the largest of two numbers using comparison operators.

x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
if x==y:
    print('both are equal')
elif x>y:
    print('x is largest')
else:
    print('y is largest')
