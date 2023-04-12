def gcd(num1, num2):
    x = num1
    y = num2
    
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    
    return x

num1 = int(input())
num2 = int(input())
print(gcd(num1, num2))