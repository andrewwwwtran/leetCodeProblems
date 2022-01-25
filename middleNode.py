# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # put node list into array then return the array //2
    # arr = [head]
    # while arr[-1].next:
    #     arr.append(arr[-1].next)
    # knowing the length of the array we can return the array // 2
    # return arr[len(arr) //2]

    # 2 pointers
    # have 1 slow pointer and another moving twice as fast
    # when the fast pointer reaches the end, the slow pointer is in the middle

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

print middleNode([1,2,3,4,5,6])