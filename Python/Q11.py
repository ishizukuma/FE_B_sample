def binSort(data):
    # index調整
    for j in range(len(data)):
        data[j] -= 1
    
    n = len(data)
    bins = [None for _ in range(n)]
    
    for i in range(n):
        bins[data[i]] = data[i]
    
    # index調整
    for k in range(n):
        bins[k] += 1
    
    return bins

print(binSort([2, 6, 3, 1, 4, 5]))