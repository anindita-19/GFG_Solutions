'''
Definition for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        curr=head
        count=0
        if head==None:
            return count
        else:
            while curr.next!=None:
                curr=curr.next
                count=count+1
            return count+1    