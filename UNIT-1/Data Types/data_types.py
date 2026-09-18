#1. Demonstrate int, float, str, bool, and complex.

a=10
b=10.4
c='jas'
d=True
e=3+4j
print(f'a={a} and type of a is {type(a)}')
print(f'b={b} and type of b is {type(b)}')
print(f'c={c} and type of c is {type(c)}')
print(f'd={d} and type of d is {type(d)}')
print(f'e={e} and type of e is {type(e)}')

#2. Accept two numbers and display their data types.

a=(int(input("Enter a age: ")))
b=(input("Enter your Name:"))
print(type(a),type(b))
print(f"Age is {a} and Name is {b}")

#3. Convert a string number into an integer and float.

a="10"
b=int(a)
c=float(a)
print(f"Value of a is {a} and type of a is {type(a)}")
print(f"Value of b is {b} and type of b is {type(b)}")
print(f"Value of c is {c} and type of c is {type(c)}")

#4. Find the length of a string.

a="hello i am jas"
print(f'length of a is {len(a)}')

#5. Create a list, tuple, set, and dictionary and display their types.

a=['apple','banana','cherry']
b=('apple','banana','cherry')
c={'apple','banana','cherry'}
d={'name':'jas','age':20}
print(f'a={a} and type of a is {type(a)}')
print(f'b={b} and type of b is {type(b)}')
print(f'c={c} and type of c is {type(c)}')
print(f'd={d} and type of d is {type(d)}')
