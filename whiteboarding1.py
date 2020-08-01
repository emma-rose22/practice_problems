#merge two sort lists
# merge two sorted linked lists and return it as a new sorted list
#the new list should be made by splicing together the nodes of the first two lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #iterate through the lists at the same time
        #insert the lower value first to the new list
        new_list = ListNode(None)
      
        l1_current = l1
        l2_current = l2
        new_current = new_list

        while l1_current:
            if l1_current and l2_current:
                #if we haven't run out of l2
                #compare, add, and increment accordingly
                if l1_current.val < l2_current.val:
                    new_current.next = ListNode(l1_current.val)
                    l1_current = l1_current.next
                    new_current = new_current.next
                else:
                    new_current.next = ListNode(l2_current.val)
                    l2_current = l2_current.next
                    new_current = new_current.next

            #if l2 ran out, just keep adding l1
            if l2_current == None:
                new_current.next = ListNode(l1_current.val)
                l1_current = l1_current.next
                new_current = new_current.next
        #if there is still l2 when l1 runs out
        #just add it until done
        while l2_current:
            new_current.next = ListNode(l2_current.val)
            l2_current = l2_current.next
            new_current = new_current.next
            
        return new_list.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #iterate through each list and add node value to array as str
        #reverse the each array
        #join and add them as ints
        #turn result into a list of str nums
        #add each number individually as ints
        l1_nums = []
        l2_nums = []
        added = []
        cur_answer = answer = ListNode(None)
        
        l1_current = l1
        l2_current = l2
        
        while l1_current:
            l1_nums.append(str(l1_current.val))
            l1_current = l1_current.next
            
        while l2_current:
            l2_nums.append(str(l2_current.val))
            l2_current = l2_current.next
            
        l1_nums = ''.join(l1_nums[::-1])
        l2_nums = ''.join(l2_nums[::-1])
        
        added = str(int(l1_nums) + int(l2_nums))
        added = added[::-1]
        
        for num in added:
            cur_answer.next = ListNode(num)
            cur_answer = cur_answer.next
            
        return answer.next
        #this works

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) 
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Idea 1: add a 'visited' property to each node as 
        # we traverse 
        # check to see if a node we're visiting has that 
        # property 
        current = head 
        
        while current is not None:
            # check if the current node has the `visited` property
            if hasattr(current, 'visited'):
                return current
            
            current.visited = True
            current = current.next 
            # if we ever encounter a node with the 'visited', then
            # we've been there before 
            # or alternatively, set the `value` to None 

        return None

 def hasCycle(self, head: ListNode) -> bool:
        # loop through the linked list 
        # look for the tail
            # if there is a tail, it's `next` is None 
            # how do we know when we've found the tail?
        
        # Idea 1: add a 'visited' property to each node as 
        # we traverse 
        # check to see if a node we're visiting has that 
        # property 
#         current = head 
        
#         while current is not None:
#             # check if the current node has the `visited` property
#             if hasattr(current, 'visited'):
#                 return True
            
#             current.visited = True
#             current = current.next 
#             # if we ever encounter a node with the 'visited', then
#             # we've been there before 
#             # or alternatively, set the `value` to None 
        
#         # we reached the end of the linked list 
#         return False
        
        # if we want to check the length of the list
        # how do we figure out the length? 
        # usually we'd figure out the length by traversing
        # until we got a node whose `next` is None
        # but if the linked list contains, we'd never get there 
        
        # What if we aren't allowed to mutate the linked list? 
        # Idea 2: Add the nodes to a set/hash table that keeps 
        # track of  nodes in the linked list we've visited 
        # as we traverse, we'll check if the current node 
        # is one we've visited before 
        # if it is, there must be a cycle, return True 
        
        # Idea 3: Traverse the linked list with two pointers,
        # one that moves at twice the speed of the other 
        # if there is a cycle in the list, then the faster 
        # runner will reach the end of the linked list 
        # otherwise, if there is a cycle, then the faster 
        # runner will lap the slower runner 
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            # increment the two pointers 
            fast = fast.next.next
            slow = slow.next 
            
            # check to see if they ever land on the same node 
            if fast is slow:
                return True
        
        # fast reached the end of the linked list 
		return False
