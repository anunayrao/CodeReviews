'''
Check if given linked list is a palindrome or not. 
You are given the head of the linked list.
checkPalindrome(head) -> Boolean value
'''
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
    
# 1 -> 2 -> 3 -> 2 -> 1

def checkPalindrome(head): # 1-> 2 -> 3  
    curr = head #1 
    reversedList_head = Node(curr.item) #1
    curr = curr.next #2
    curr1 = reversedList_head.next #None
    while curr: 
        curr1 = Node(curr.item) #2 3
        curr1 = curr1.next #None None
        curr = curr.next #3 None
    
    
    
    prev = reversedList_head #1
    #curr = prev
    curr = prev.next #2
    while curr:
        temp = curr.next #3 None
        curr.next = prev # 2 -> 1 , 3 -> 2
        prev = curr #2 3
        curr = temp #3 None
    curr = head
    curr1 = reversedList_head
    while curr:
        if curr != curr1:
            return False
        curr = curr.next
        curr1 = curr.next
    return True 