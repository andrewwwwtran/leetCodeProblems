# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def reverseString(s):

    # simple way to do this is
    # using 2 pointers and swapping 
    left = 0 
    right = len(s) - 1
    while left < right:
        # temp = s[i]
        # s[i] = s[j]
        # s[j] = temp
        s[left], s[right] = s[right], s[left] # instead of using a temp
        # move pointers towards center of array
        left += 1
        right -= 1
    
