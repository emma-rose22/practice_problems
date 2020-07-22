'''You are given a NxM integer array matrix with space separated elements (N= rows and M= columns).
Your task is to print the transpose and flatten results.'''

import numpy as np

nums = input().split()
nums = nums + input().split()
nums = nums + input().split()
nums = [int(i) for i in nums]
nums = np.array(nums)
#nums.shape = (2, 2)

print(np.transpose(nums))

print(nums)
print(nums.flatten())