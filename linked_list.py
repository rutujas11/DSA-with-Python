class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
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
    
    def insert_after(self,prev_data,data):
        curr = self.head
        while curr and curr.data != prev_data:
            curr = curr.next
        if curr is None:
            print("provided node is not present!!!")
            return
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    def delete_value(self,data):
        curr = self.head
        if curr is not None:
            if curr.data == data:
                self.head = curr.next 
                curr = None
                return
        prev = None
        while curr is not None:
            if curr.data == data:
                break
            prev = curr
            curr = curr.next

            if curr is None:
                return
            
        prev.next = curr.next
        curr = None

    def search(self,data):
        curr = self.head
        while curr:
            if curr.data == data:
                print(data,"found in the list")
                return True
            curr = curr.next
        print(f"{data} not found in the list")

    def get_length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        print(f"length of list is {count}")

    def printll(self):
        curr = self.head
        while curr:
            print(curr.data,end=" ----> ")
            curr = curr.next
        print("Null")



if __name__ == "__main__":
    llist = Linkedlist()
    llist.insert_begin(30)
    llist.insert_end(67)
    llist.insert_end(36)
    llist.insert_end(40)
    llist.insert_after(36,45)
    llist.delete_value(30)
    llist.insert_after(40,42)
    llist.delete_value(36)
    llist.printll()
    llist.search(40)
    llist.get_length()


    