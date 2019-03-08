class Sort(object):
    def QuickSort(self, nums):
        self.__qsort(nums, 0, len(nums) - 1)

    def __qsort(self, nums, p, r):
        if p < r:
            q = self.__partition(nums, p, r)
            self.__qsort(nums, p, q - 1)
            self.__qsort(nums, q + 1, r)

    def __partition(self, nums, p, r):
        i = p - 1
        for j in range(p, r):
            if nums[j] <= nums[r]:
                i += 1
                self.__swap(nums, i, j)
        self.__swap(nums, i + 1, r)
        return i + 1

    def __swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
