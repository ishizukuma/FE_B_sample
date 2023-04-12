class ListElement:
    def __init__(self, val):
        self.val = val
        self.next = None

listHead = None

def append(qVal):
    global listHead
    curr = ListElement(qVal)
    
    if listHead is None:
        listHead = curr
    else:
        prev = listHead
        while prev.next is not None:
            prev = prev.next
        prev.next = curr
    
    return listHead

print(append("A"))