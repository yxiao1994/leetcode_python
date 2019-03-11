class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
        record = set()
        i = 0
        j = 0
        res = 0
        while j < len(s):
            if s[j] not in record:
                record.add(s[j])
                j += 1
                res = max(res, j - i)
            else:
                record.remove(s[i])
                i += 1
        return res

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1
        while low <= high:
            mid = low + (high - low) / 2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorderhelp(root, res)
        return res

    def inorderhelp(self, root, l):
        if not root:
            return
        else:
            self.inorderhelp(root.left, l)
            l.append(root.val)
            self.inorderhelp(root.right, l)

    def TreeDepth(self, root):

        if not root:
            return 0

        return max(self.TreeDepth(root.left), self.TreeDepth(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        leftDepth = self.TreeDepth(root.left)
        rightDepth = self.TreeDepth(root.right)
        return abs(leftDepth - rightDepth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        return self.buildTreeHelper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def buildTreeHelper(self, preorder, pStart, pEnd, inorder, inStart, inEnd):
        if pStart > pEnd or inStart > inEnd:
            return None
        val = preorder[pStart]
        index = inStart
        while index <= inEnd and inorder[index] != val:
            index += 1
        if index > inEnd:
            raise RuntimeError('input error!')
        root = TreeNode(val)
        leftLen = index - inStart
        root.left = self.buildTreeHelper(preorder, pStart + 1, pStart + leftLen,
                                         inorder, inStart, index - 1)
        root.right = self.buildTreeHelper(preorder, pStart + 1 + leftLen, pEnd,
                                          inorder, index + 1, inEnd)
        return root

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = [root]
        while len(queue) != 0:
            level_value = []
            num = len(queue)
            for i in range(num):
                node = queue.pop(0)
                level_value.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_value)
        return res

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not candidates:
            return res
        curr = []
        self.combinationSumHelper(candidates, target, 0, res, curr)
        return res

    def combinationSumHelper(self, candidates, target, start, res, curr):
        if target < 0:
            return
        elif target == 0:
            res.append(list(curr))
            return
        else:
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                self.combinationSumHelper(candidates, target - candidates[i], i, res, curr)
                curr.pop()


