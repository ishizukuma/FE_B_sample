array = [1, 2, 3, 4, 5]

for left in range(len(array)//2):
    right = len(array) - left - 1
    tmp = array[right]
    array[right] = array[left]
    array[left] = tmp

print(array)