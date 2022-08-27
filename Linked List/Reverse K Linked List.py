class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    def reverseKgroup(self, head, k):
        ptr = head
        next = None
        prev = None
        count = 0

        while (ptr is not None and count < k):
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next
            count += 1

        if (next is not None):
            head.next = self.reverseKgroup(next, k)
        return prev

    def insert(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def printLL(self): 
        temp = self.head 
        while(temp): 
            print (temp.data, end = ' ') 
            temp = temp.next

# Driver Code

if __name__ == '__main__':

    list1 = LinkedList() 
    list1.insert(4)
    list1.insert(2) 
    list1.insert(8)
    list1.insert(5) 
    list1.insert(1) 
    list1.insert(6) 
    list1.insert(3) 
    list1.insert(7)

    print("Given Linked List is: ")
    list1.printLL()
    print()
    list1.head = list1.reverseKgroup(list1.head, 3)

    print("Reverese Linked List is: ")
    list1.printLL()