def order(n):
    if len(tree[n]) == 2:
        order(tree[n][0]-1)
        print(n+1)
        order(tree[n][1]-1)
    elif len(tree[n]) == 1:
        order(tree[n][0]-1)
        print(n+1)
    else:
        print(n+1)

tree = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14], [], [], [], [], [], [], []]
order(0)
# 出力結果：8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7