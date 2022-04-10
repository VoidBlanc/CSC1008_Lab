class SinglyNode:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, val):
        node = SinglyNode(val)
        
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = node
            
                  
    def deleteAt(self, index):
        count = 0
        prev = None
        
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            while temp is not None:
                if count == index:
                    prev.next = temp.next
                    temp = temp.next
                else:
                    prev = temp
                    temp = temp.next
                count += 1
            del temp

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next 

