def findRank(sortedData, p):
    i = round(p * (len(sortedData) - 2))
    return sortedData[i+1] if p != 0 else sortedData[i]

def summarize(sortedData):
    rankData = []
    p = [0, 0.25, 0.5, 0.75, 1]
    
    for i in range(len(p)):
        rankData.append(findRank(sortedData, p[i]))
    
    return rankData

print(summarize([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))