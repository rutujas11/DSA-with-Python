# Implementation of Queue Using collections.deque (Efficient for Queue Operations)

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Dequeue (deleted) element is : ",self.queue.popleft())
            print("Queue after dequeue :---> ",list(self.queue))

    def front_elet(self):
        if self.is_empty():
            print("queue is empty")
        else:
            print("Front element is : ",self.queue[0])

    def rare_elt(self):
        if self.is_empty():
            print("queue is empty")
        else:
            print("Rare element is : ",self.queue[len(self.queue)-1])

    def size(self):
        print("Size of queue is : ",len(self.queue))

    def print(self):
        if self.is_empty():
            print("queue is empty")
        else:
            print("Queue :---> ",list(self.queue))

    def is_empty(self):
        return len(self.queue)==0
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(14)
    q.enqueue(24)
    q.enqueue(34)
    q.enqueue(54)
    q.enqueue(54)
    q.enqueue(64)
    q.print()
    q.dequeue()
    q.front_elet()
    q.rare_elt()
    q.size()