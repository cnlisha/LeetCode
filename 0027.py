class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        m = length
        for i in range(length):
            if (nums[i]==val):
                nums[i] = 101
                m -= 1
        # nums.sort() # 升序排序

        # 冒泡排序
        for i in range(length-1): # 遍历 len(nums)-1 次
            for j in range(length-i-1): # 已排好序的部分不用再次遍历
                if (nums[j]>nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j] # Python 交换两个数不用中间变量
        return m
