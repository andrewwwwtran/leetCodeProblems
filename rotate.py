# Given an array, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

def rotate(nums,k):
    
    # iterative
    # time: O(n) space: O(n)
    for i in range(k % len(nums)):
        nums.insert(0, nums.pop(len(nums)-1))
    
    # another way to do this 
    # grab the k to end of list numbers
    # insert those to the front
    # left side = [-k:]
    # right side = [:-k]
    k = k % len(nums)
    nums[:] = nums[:-k] + nums[-k:]