'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        a=Node(x)
        curr=head
        
        if head == None:
            return a
        while curr.next!=None:
            curr=curr.next
        curr.next=a
        a.next=None
        return head
        