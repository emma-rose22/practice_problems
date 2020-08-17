'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''

class Solution:
    def reverse(self, x: int) -> int:
        l = list(str(x))
        #handle negatives
        neg = False
        #handle empty or single input
        if len(l) == 1:
            return x

        #handle negatives
        if l[0] == '-':
            l.remove('-')
            neg = True

        answer = l[::-1]
        
        #getting rid of zeros in front 
        while answer[0] == '0':
            answer.remove('0')
        if neg:
            answer.insert(0, '-')
        return ''.join(answer)