def search(data, target):
    
    low = 0
    high = len(data) - 1
    
    while low <= high:
        middle = (low + high) // 2
        if data[middle] < target:
            low = middle
        elif data[middle] > target:
            high = middle
        else:
            return middle
        
    return -1

print(search([1,2], 2)) # 無限ループすることに注意