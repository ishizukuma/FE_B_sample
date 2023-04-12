def pow(a, b):
    return a**b

def calc(x, y):
    return pow(pow(x, 2) + pow(y, 2), 0.5)

x = int(input())
y = int(input())
print(calc(x, y))