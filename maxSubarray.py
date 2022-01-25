# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:

# Input: nums = [1]
# Output: 1

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

def maxSubarray(self, nums):
    # base case
    if len(nums) == 0: # if not nums: return 0
        return 0
    
    # Kadane's Algorithm
    bestSum = nums[0]
    currentSum = nums[0]

    for x in nums[1:]:
        currentSum = max(x, currentSum + x)
        bestSum = max(bestSum, currentSum)
    return bestSum