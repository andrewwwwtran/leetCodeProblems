# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true


def isValid(s):

    # listOfOpenChar = ["(", "[", "{"]
    # listOfClosedChar = [")", "]", "}"]

    # tempList = []

    # if len(s) == 1:
    #     return False

    # # use a stack
    # for openChar in input:
    #     if openChar in listOfOpenChar:
    #         # tempList.append(openChar)
    #         tempList.append(openChar)
    #     # read in a closed parenthesis
    #     elif openChar in :
    #         tempList.pop()
            
    # print openList

    # if not tempList:
    #     # empty list
    #     return True
    # else:
    #     return False

    # use a dictionary and a stack
    stack = [] 
    # map closed to open
    paranthesesDict = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    for c in s:
        if stack and c in paranthesesDict and paranthesesDict[c]==stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    return not stack

# print isValid("()") # true 
# print isValid("(){}[]") # true
# print isValid("))") # false