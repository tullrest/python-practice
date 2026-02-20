# =============================================
# Basic function examples
# =============================================
def say_hello():
    print("Hello!")

say_hello()

name = input("What is your name? ")
print("Hello,", name)

a = int(input("a: "))
b = int(input("b: "))
print("a+b =", a+b)

msg = input("Message: ")
print(msg)
print(msg)
print(msg)

age = int(input("Your age: "))

if age >= 20:
    print("Adult")

age = int(input("Your age:"))

if age >= 20:
    print("Adult")
else:
    print("Not adult")

score = int(input("Score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C or lower")

for i in range(5):
        print(i)

x = 0

while x < 5:
    print(x)
    x += 1

number = int(input("Number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

number = int(input("number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

for i in range(1,31):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# ============================================
# Tilting logic
# ============================================
def is_tilting(andgle_deg, threshold=5):
    if abs(angle_deg) > threshold:
        return True
    else:
        return False
    
print(is_tilting(3))
print(is_tilting(10))
print(is_tilting(-8))