def say_hello():
    print("Hello!")

say_hello()

def say_hello(name):
    print("Hello,",name)

say_hello("Junhyung")

def add(a, b):
    result = a + b
    return result

sum_value = add(3,4)
print("sum =", sum_value)

def is_tilting(andgle_deg, threshold=5):
    if abs(angle_deg) > threshold:
        return True
    else:
        return False
    
print(is_tilting(3))
print(is_tilting(10))
print(is_tilting(-8))