#You are given two non-empty linked lists representing two non-negative integers. The #digits are stored in reverse order, and each of their nodes contains a single digit. Add #the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        
        
        curr=l1
        i=0
        result1=0
        while curr!=None:
            result1+=(10**i)*curr.val
            curr=curr.next
            i+=1

        curr=l2
        i=0
        result2=0
        while curr!=None:
            result2+=(10**i)*curr.val
            curr=curr.next
            i+=1
        
        result3=result1+result2
        print(result3)
        head=None
        if result3==0:
            new_node=ListNode(val=0,next=None)
            head=new_node
            return head
        while result3 != 0:
            if head==None:
                new_node=ListNode(val=result3 %10,next=None)
                head=new_node
                result3=result3//10
                continue
            
            curr=head
            while curr.next!=None:
                curr=curr.next
            new_node=ListNode(val=result3 %10,next=None)
            curr.next=new_node

            result3=result3//10
        return head

