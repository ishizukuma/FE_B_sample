class ListElement:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def delNode(pos):
    global listHead
    if pos == 1:
        listHead = listHead.next
    else:
        prev = listHead
        for i in range(2, pos):
            prev = prev.next
            if prev is None:
                return
        prev.next = prev.next.next


# テストケース
if __name__ == '__main__':
    # リストを初期化
    listHead = ListElement(1, ListElement(2, ListElement(3, ListElement(4, ListElement(5)))))

    # リストの要素を表示
    current = listHead
    while current is not None:
        print(current.value, end=' ')
        current = current.next
    print()

    # 2番目の要素を削除
    delNode(2)

    # 削除後のリストの要素を表示
    current = listHead
    while current is not None:
        print(current.value, end=' ')
        current = current.next
    print()

    # 1番目の要素を削除
    delNode(1)

    # 削除後のリストの要素を表示
    current = listHead
    while current is not None:
        print(current.value, end=' ')
        current = current.next
    print()

    # 3番目の要素を削除
    delNode(3)

    # 削除後のリストの要素を表示
    current = listHead
    while current is not None:
        print(current.value, end=' ')
        current = current.next
    print()
    
"""
1 2 3 4 5 
1 3 4 5 
3 4 5 
3 4 
"""