def simRatio(s1, s2):
    cnt = 0
    
    if len(s1) != len(s2):
        return -1
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            cnt = cnt + 1
    
    return cnt / len(s1)

print(simRatio(["a", "p", "p", "l", "e"], ["a", "p", "p", "l", "e"]))
print(simRatio(["a", "p", "p", "l", "e"], ["a", "p", "r", "i", "l"]))
print(simRatio(["a", "p", "p", "l", "e"], ["m", "e", "l", "o", "n"]))
print(simRatio(["a", "p", "p", "l", "e"], ["p", "e", "n"]))