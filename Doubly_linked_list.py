class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class doublyll:
    def __init__(self):
        self.head = None

## Insertion
    def insert_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev= new_node
            self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insert_after(self,prev_node,data):
        curr = self.head
        while curr and curr.data != prev_node:
            curr = curr.next
        if curr is None:
            print(f"node {prev_node} is not present in the list!!!")
            return
        new_node = Node(data)
        new_node.next=curr.next
        curr.next = new_node
        new_node.prev = curr
        if new_node.next:
            new_node.next.prev = new_node

## Deletion
    def delete_value(self,value):
        if self.head is None:
            print("List is empty")
            return
        
        curr = self.head
        while curr:
            if curr.data == value:
                if curr == self.head:
                    self.head = curr.next
                    if self.head:
                        self.head.prev = None
                else:  
                    if curr.next:
                        curr.next.prev = curr.prev
                    if curr.prev:
                        curr.prev.next = curr.next
                    
                next_node = curr.next
                del curr
                curr = next_node
            else:
                curr = curr.next

## Searching
    def search(self,data):
        curr = self.head
        while curr:
            if curr.data == data:
                print(data,"found in the list")
                return True
            curr = curr.next
        print(f"{data} not found in the list")

## length
    def get_length(self):
        if self.head is None:
            print("list is empty!!!")
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        print(f"Length of list is {count}") 

## Display
    def printll(self):
        curr = self.head
        while curr:
            print(curr.data,end = " ----> ")
            curr = curr.next
        print("Null")

if __name__ == "__main__":
    llist = doublyll()
    llist.insert_begin(34)
    llist.insert_begin(44)
    llist.insert_begin(54)
    llist.insert_end(24)
    llist.insert_end(14)
    llist.insert_end(4)
    llist.insert_after(40,46)
    llist.insert_after(14,46)
    llist.delete_value(24)
    llist.search(54)
    llist.search(100)
    llist.printll()
    llist.get_length()