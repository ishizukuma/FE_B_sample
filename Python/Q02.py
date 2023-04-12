def fizzBuzz(num):
    result = ""
    
    if  num % 3 == 0 and num % 5 == 0:
        result = "3と5で割り切れる"
    elif num % 3 == 0:
        result = "3で割り切れる"
    elif num % 5 == 0:
        result = "5で割り切れる"
    else:
        result = "3でも5でも割り切れない"
    
    return result

print(fizzBuzz(int(input())))