'''
Check if given linked list is a palindrome or not. 
You are given the head of the linked list.
checkPalindrome(head) -> Boolean value
'''
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

def checkPalindrome(head): # 1-> 2 -> 3  
    curr = head #1 
    #reversedList_head = Node(curr.item) #1
    reverseCopy = Node(head.item)
    curr = curr.next #2
    #curr1 = reversedList_head.next #None
    curr1 = reverseCopy
    
    while curr: 
        #curr1 = Node(curr.item) #2 3
        curr1.next = Node(curr.item)
        curr1 = curr1.next #None None
        curr = curr.next #3 None
    
    
    printList(reverseCopy)
    #prev = reversedList_head #1
    prev = reverseCopy
    #curr = prev
    curr = prev.next #2
    while curr:
        temp = curr.next #3 None
        curr.next = prev # 2 -> 1 , 3 -> 2
        prev = curr #2 3
        curr = temp #3 None
    curr = head
    curr1 = prev
    #curr1 = reversedList_head -> Not reversed copy
    while curr:
        if curr.item != curr1.item: #logical error
            return False
        curr = curr.next
        curr1 = curr1.next #logical error
    return True 

def printList(node):
    while node:
        print(node.item)
        node = node.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    print(checkPalindrome(head))