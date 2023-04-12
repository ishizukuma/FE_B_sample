def prioSched():
    class PrioQueue:
        def __init__(self):
            self.queue = []
        
        def enqueue(self, item, priority):
            self.queue.append((item, priority))
            self.queue.sort(key=lambda x: x[1])
        
        def dequeue(self):
            if len(self.queue) == 0:
                return None
            return self.queue.pop(0)[0]
        
        def size(self):
            return len(self.queue)

    prioQueue = PrioQueue()
    prioQueue.enqueue("A", 1)
    prioQueue.enqueue("B", 2)
    prioQueue.enqueue("C", 2)
    prioQueue.enqueue("D", 3)
    prioQueue.dequeue()
    prioQueue.dequeue()
    prioQueue.enqueue("D", 3)
    prioQueue.enqueue("B", 2)
    prioQueue.dequeue()
    prioQueue.dequeue()
    prioQueue.enqueue("C", 2)
    prioQueue.enqueue("A", 1)
    while prioQueue.size() != 0:
        print(prioQueue.dequeue())

prioSched()
# 出力結果：A　C　D　D