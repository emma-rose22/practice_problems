#this problem is incomplete 

'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray
in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the 
whole array sorted in ascending order.
'''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #find a subarray that needs to be sorted
        #for the whole array to be sorted
        
        #have a counter at both ends
        #have a largest int index position var
        #have a smallest in index positin var
        #while the left index doesnt reach largest int and
        #right doesnt reach smallest int
            #increment counters
        #subtract the smallest index position from largest and return
        
        l = 0
        #index position, largest value
        l_large = (0, 0)
        r = len(nums) - 1
        #index position, smallest value
        r_small = (r ,nums[r])
        
        if len(nums) == 1:
            return 0
        
        run = True
        while run:
            if nums[l] < nums[r]:
                l += 1
                r -= 1
                if nums[l] > l_large[1]:
                    l_large = (l, nums[l])
                if nums[r] < r_small[1]:
                    r_small = (r, nums[r])
                if l == r:
                    print('???')
                    r_small = (1, 0)
                    l_large = (2, 0)
                    run = False
                else:
                    print('?', r_small)
                    run = False
            #this is if the whole thing needs to be sorted
            else:
                return l_large[0] + r_small[0] + 1
                    

        if (l_large[1] + 1) == r_small[1]:
            return 0 
        
        return (r_small[0] - l_large[0]) + 1
            