def fact(a):
    if a == 0 or a == 1:
        return 1
    else:
        res = 1
        for i in range(2, a + 1):
            res *= i
        return res
    

x = int(input("Enter a number: "))

print(f"Factorial of {x} is: ", fact(x))