# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

def searchInsert(self, nums, target):

    # time O(n)
    # for i in range(len(nums)):
    #     if target == nums[i]:
    #         return i
    
    # o(log n) is binary search
    start = 0
    end = len(nums)-1
    midpoint = (start + end) / 2

    # print midpoint, nums[midpoint]

    while(start < end):
        # case target is found
        if(target == nums[midpoint]):
            return midpoint
        # target is a num between
        # elif(target > nums[midpoint] and target < nums[midpoint+1]):
        #     return midpoint+1
        elif(target < nums[midpoint]):
            end = midpoint-1
            midpoint = (start + end) / 2
        elif(target > nums[midpoint]):
            start = midpoint+1
            midpoint = (start + end) / 2
    
    # return end
        if(start >= end):
            if(target > nums[midpoint]):
                return midpoint+1
            else:
                return midpoint-1

    # recursive
    if len(nums) == 0:
        return 0
    
    N = len(nums)
    mid = N / 2
    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return self.searchInsert(nums[:mid], target)
    else:
        result = self.searchInsert(nums[mid+1:], target)
        return result + mid + 1
# print searchInsert([1,3,5,6], 5) # return 2

# print searchInsert([1,3,5,6], 0) # return 1