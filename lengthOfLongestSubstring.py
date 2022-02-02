# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.



def lengthOfLongestSubstring(s):
    # sliding window algorithm

    subArr = []
    maxSubLength = 0
    for i in range(len(s)):
        if s[i] in subArr:
            # subArr.clear()
            indexOfrepeat = subArr.index(s[i])
            del subArr[:indexOfrepeat+1]
            subArr.append(s[i])
        else:
            subArr.append(s[i])
        maxSubLength = max(len(subArr), maxSubLength)
        print subArr
    return maxSubLength


print lengthOfLongestSubstring("ckilbkd")