# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

def palindrome(num):

    numList = []
    tempNum = 0

    start = 0
    end = 0
    

    if(num < 0):
        return False
    
    while(num > 0):
        tempNum = num % 10
        num = num / 10
        numList.append(tempNum)
    
    end = len(numList)-1
    while(end > 0):
        if(numList[start] != numList[end]):
            return False
        start += 1
        end -= 1
    
    return True


    # another way to do this is
    # tostring the number and .reverse the string and compare 


# print palindrome(123)

# print palindrome(1221)

# print palindrome(-10)

# print palindrome(121)
