class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        res = []
        for i, num in enumerate(nums):
            dic[num] = i
        for i, num in enumerate(nums):
            e = target - num
            if e in dic and dic[e] > i:
                res += [i, dic[e]]
        return res

    def createList(self, l):
        """
        create linked list
        :param l: a list
        :return: a linked list contains elements in l
        """
        head = ListNode(l[0])
        curr = head
        for i in range(1, len(l)):
            curr.next = ListNode(l[i])
            curr = curr.next
        return head

    def printList(self, head):
        """
        print linked list
        :param head: head of linked list
        :return:
        """
        p = head
        while p:
            print(str(p.val), end="")
            p = p.next
            if p:
                print("->", end="")

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        sum = 0
        while l1 or l2:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            sum += (val1 + val2)
            curr.next = ListNode(sum % 10)
            sum = sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        if sum == 1:
            curr.next = ListNode(1)
        return dummy.next

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

