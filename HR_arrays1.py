'''You are given a space separated list of nine integers. Your task is to convert this list into a 3x3 NumPy array.'''

import numpy as np

nums = input().split()
nums = [int(i) for i in nums]
nums = np.array(nums)
nums.shape = (3, 3)
print(nums)
