# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]


# def twoSums(nums, target):

#     # time O(n^2)
#     # space O(1)
#     for i in range(len(nums)):
#         j = i + 1
#         while j < len(nums):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#     return None


def twoSumsMap(nums, target):
    # define a map
    seenMap = {} 
    
    for i, val in enumerate(nums):
        # print [i, val]
        lookingFor = target - val
        if lookingFor in seenMap:
            return [seenMap[lookingFor], i+1]
        else:
            seenMap[val] = i+1

    # another solution 
    # using 2 pointers
    # i = 0
    # j = len(nums)-1
    # while i < j:
    #     if nums[i] + nums[j] == target:
    #         return [i+1, j+1]
    #     elif nums[i] + nums[j] < target:
    #         i += 1
    #     else:
    #         j -= 1

print twoSumsMap([2,7,11,15], 9) # [0,1]
print twoSumsMap([3,2,4], 6) # [1,2]
    
