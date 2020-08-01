'''
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.

You may assume that each input would have exactly one solution, and
you may not use the same element twice.
'''

def twoSum(self, nums: List[int], target: int) -> List[int]:
    #idea is to store each number and its index position in dict
    #whil doing this, we subtract from the target the number
    #if that output exists already in the dict, we have found our two numbers
    # we then call on the dict for the stored index position for the first number
    #and i is the index for the second one, we return them together
    index_mapping = {}
    #using range instead of directly iterating will keep our index position
    for i in range(len(nums)):
        current = nums[i]
        compliment = target - current
        #is compliment in dictionary?

        if compliment in index_mapping:
            return [index_mapping[compliment], i]

        else:
            index_mapping[current] = i 



'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''
from collections import deque

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.stack = deque()
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.size += 1
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.size -= 1
        return self.stack.popleft()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size > 0:
            return False
        else:
            return True

'''
apparently this solution is faster, but I woner if 
that is due to a small test size?

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.stack = []
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.size += 1
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.size -= 1
        to_remove = self.stack[0]
        self.stack.remove(to_remove)
        return to_remove
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size > 0:
            return False
        else:
            return True
'''


'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a dictionary for each word
        #set of word as key, og word as value
        #go through and return all values for each key
        cache = {}
        for word in strs:
            s = list(word)
            #this way all the letters are in the same order for different words
            #dictionary can't handle list
            #moved sorting here so that way it can happen in one line
            s = ''.join(sorted(s))
            #if the set of the word has been found, add the word to the list of 
            #grouped words
            if s in cache:
                cache[s].append(word)
            else:
                cache[s] = [word]
            
        return cache.values()
        