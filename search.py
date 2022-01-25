# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # base case
    
    start = 0 
    end = len(nums) # len(nums)-1
    # mid = end / 2
    
    while(start < end):
        mid = start + (end - start) // 2 # avoid overflow bc [mid = (start + end) / 2] causes overflow
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            # left side of array
            end = mid # end = mid - 1
            # mid = (start + end) / 2
        else:
            # right side
            start = mid+1
            # mid = (start + end) / 2

    return -1