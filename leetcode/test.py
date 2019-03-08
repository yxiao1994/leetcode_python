from leetcode.top100 import Solution
from leetcode.sort import Sort

if __name__ == '__main__':
    # obj = Solution()
    # root = obj.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    # print(obj.levelOrder(root))
    # print(obj.twoSum([1, 2, 3, 7], 8))
    # obj.printList(obj.lengthOfLongestSubstring('abcabcbb'))
    obj = Sort()
    nums = [1, 4, 5, 7, 6, 9, 9, 11, 8, 0, -2]
    obj.HeapSort(nums)
    print(nums)