def makeNewArray(in_list):
    out = []
    out.append(in_list[0])
    
    for i in range(1, len(in_list)):
        tail = out[len(out)-1]
        out.append(tail + in_list[i])
    
    return out

result = makeNewArray([3,2,1,6,5,4])
print(result, "\nanswer = ",result[4])