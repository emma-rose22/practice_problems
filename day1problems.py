'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if
every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

        #works

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order 
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

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

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position 
(0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

'''

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
