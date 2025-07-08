def add(a,b):
    return a + b

def sub(a,b):
    return a - b
    
def multi(a,b):
    return a * b

def div(a,b):
    return a / b


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("Addition: ", add(x,y))
print("Subtraction: ", sub(x,y))
print("Multiplication: ", multi(x,y))
print("Division: ", div(x,y))