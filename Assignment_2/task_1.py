def iseven(a):
    if(a % 2 == 0):
        return 0
    else:
        return 1
    
x = int(input("Enter a number: "))
res = iseven(x)

if res == 0:
    print(f"{x} is an even number.")
else:
    print(f"{x} is an odd number.")