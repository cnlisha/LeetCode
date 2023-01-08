class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 二分查找
        left = 0
        right = len(nums) - 1
        while (left<=right):
            middle = int((left+right)/2)
            if (nums[middle]==target):
                return middle
            elif (nums[middle]<target):
                left = middle  +1
            else:
                right = middle - 1
        return left
