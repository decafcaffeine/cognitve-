# Assignment 1.1
# WAP to print your name three times

for i in range(3):
    print("Your Name")

# Assignment 2.1
# WAP to add three numbers and print the result

a = 10
b = 20
c = 30

sum = a + b + c

print("Sum =", sum)

# Assignment 2.2
# WAP to concatenate three strings and print the result

a = "Bhagat"
b = " "
c = "Singh"

result = a + b + c

print(result)


# Assignment 4.1
# WAP to print the table of 7


for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
    print()

# WAP to print the table of 9

for i in range(1, 11):
    print("9 x", i, "=", 9 * i)

# Assignment 4.2
# WAP to print the table of n (input by user)

n = int(input("Enter a number: ")

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# Assignment 4.3
# WAP to add all numbers from 1 to n

n = int(input("Enter a number: "))

s = 0

for i in range(1, n + 1):
    s = s + i

print("Sum =", s)

# Assignment 5.1
# WAP to find maximum among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Maximum =", a)
elif b >= a and b >= c:
    print("Maximum =", b)
else:
    print("Maximum =", c)
  

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum =", max(a, b, c))


# Assignment 5.2
# WAP to add all numbers divisible by 7 and 9 from 1 to n

n = int(input("Enter n: "))
s = 0
for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        s = s + i

print("Sum =", s)

# Assignment 5.3
# WAP to add all prime numbers from 1 to n

n = int(input("Enter n: "))
sum = 0
for num in range(2, n + 1):
    prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        sum = sum + num

print("Sum of Prime Numbers =", sum)



# Assignment 6.1
# WAP using function to add all odd numbers from 1 to n

def AddOdd(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            s = s + i
    return s


n = int(input("Enter n: "))
print("Sum of Odd Numbers =", AddOdd(n))


# Assignment 6.2
# WAP using function to add all prime numbers from 1 to n

def IsPrime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True
def AddPrime(n):
    s = 0
    for i in range(2, n + 1):
        if IsPrime(i):
            s = s + i
    return s
n = int(input("Enter n: "))
print("Sum of Prime Numbers =", AddPrime(n))
