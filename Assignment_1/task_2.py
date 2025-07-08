def greet(fname, lname):
    full_name = fname + " " + lname
    print(f"Hello, {full_name}! Welcome to the Python program.")


x = str(input("Enter your first name: "))
y = str(input("Enter your last name: "))

greet(x,y)