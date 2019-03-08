class Sort(object):
    def QuickSort(self, nums):
        """
        对nums数组快速排序
        :param nums: a list
        :return:
        """
        self.qsort(nums, 0, len(nums) - 1)

    def qsort(self, nums, p, r):
        if p < r:
            q = self.partition(nums, p, r)
            self.qsort(nums, p, q - 1)
            self.qsort(nums, q + 1, r)

    def partition(self, nums, p, r):
        i = p - 1
        for j in range(p, r):
            if nums[j] <= nums[r]:
                i += 1
                self.swap(nums, i, j)
        self.swap(nums, i + 1, r)
        return i + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def maxHeapfy(self, nums, i, n):
        """
        调整堆
        :param nums:
        :param i:the index of element needed to adjust
        :param n:num of elements in the heap
        :return:
        """
        while i < n:
            child = 2 * i + 1
            if child >= n:
                break
            if child + 1 < n and nums[child + 1] > nums[child]:
                child += 1
            if nums[child] > nums[i]:
                self.swap(nums, i, child)
                i = child
            else:
                break

    def buildHeap(self, nums):
        """
        建大根堆
        :param nums: a list
        :return: max_heap
        """
        i = len(nums) // 2
        while i >= 0:
            self.maxHeapfy(nums, i, len(nums))
            i -= 1

    def HeapSort(self, nums):
        self.buildHeap(nums)
        i = len(nums) - 1
        while i > 0:
            self.swap(nums, 0, i)
            self.maxHeapfy(nums, 0, i)
            i -= 1
