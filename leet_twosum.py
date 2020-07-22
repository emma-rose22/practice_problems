'''given an array of integers, return indices of the two numbers such that they add up to a specific problem

given nums = [2, 7, 11, 15], target = 9

because nums[0] + nums[1] = 2 + 7 = 9
return [0, 1]

'''

#this is a great time to use a hash table

#class Solution(object):
def twoSum(nums, target):
    index_mapping = {}

    # go through the nums
    # access to that number
    # target - number, we can store this in a dictionary
    #if compliment is in dictionary
        #return the indicies 
    # else put number in dictionary

    #go through everything 
    for i in range(len(nums)):
        #look at the acutal value at index
        current = nums[i]
        #do the maths
        compliment = target - current

        #is compliment in dictionary?
        if compliment in index_mapping:
            return [index_mapping[compliment], i]

        else:
            index_mapping[current] = i 


print(twoSum([2,7,11,15], 9))