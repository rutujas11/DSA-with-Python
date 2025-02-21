# 1) Optimized Stack Implementation using "collections.deque"
'''- The most efficient way to implement a stack in Python is by using collections.deque
   - As it provides O(1) time complexity for both push (append) and pop operations.'''

from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("stack has no elements to return")
        print("Element jsut poped : ",self.stack.pop())
        print("Stack after poping the element :----> ",list(reversed(self.stack)))
    
    def top_elt(self):
        if self.is_empty():
            print("stack is empty")
        print("Top element is : ",self.stack[-1])
    
    def length(self):
        print("length of stack : ",len(self.stack))
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def print(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("stack elements from top to bottom:----> ",list(reversed(self.stack)))


if __name__ == "__main__":
    print("This is stack implementation using a collections.deque")
    mystack = Stack()
    mystack.push(5)
    mystack.push(15)
    mystack.push(25)
    mystack.push(35)
    mystack.push(45)
    mystack.push(55)
    mystack.push(65)
    mystack.print()
    mystack.pop()
    mystack.top_elt()
    mystack.length()


# 2) Using a Python List (Simplest Way)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        print("just popped element is : ",self.stack.pop())
        print("Stack after poping the element :----> ",list(reversed(self.stack)))
    
    def top_elt(self):
        if self.is_empty():
            print("stack is empty")
        print("Top element is : ",self.stack[-1])
    
    def length(self):
        print("length of stack : ",len(self.stack))
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def print(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("stack elements from top to bottom:----> ",list(reversed(self.stack)))


if __name__ == "__main__":
    
    print("------------------------------------------------------------------------------------------------------------------")
    print("This is stack implementation using a Python List (Simplest Way)")
    s = Stack()
    s.push(5)
    s.push(15)
    s.push(25)
    s.push(35)
    s.push(45)
    s.push(55)
    s.push(65)
    s.print()
    s.pop()
    s.top_elt()
    s.length()

    