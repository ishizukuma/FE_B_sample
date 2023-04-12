def fee(age):

    if age <= 3:
        ret = 100
    elif age <= 9:
        ret = 300
    else:
        ret = 500
    
    return ret

print(fee(int(input())))