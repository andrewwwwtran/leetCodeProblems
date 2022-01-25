# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"

def reverseWords(s):
    # 2 pointers
    left = 0
    right = 0
    solution = []
    while right < len(s):
        if s[right] == ' ':
            currentWord = s[left:right]
            solution.append(currentWord[::-1])
            left = right + 1
        right += 1

    # to grab the last word
    solution.append(s[left:right][::-1])
    return " ".join(solution)

    # for i, value in enumerate(s):
    #     if value == ' ':
    #         currentWord = s[]
    #         right = i-1
    #         while(left < right):
    #             solution[left], solution[right] = solution[right], solution[left]
    #             left += 1
    #             right -= 1
            

print reverseWords("Hello world")