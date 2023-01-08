class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 快慢指针法
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while (fast<n):
            if (nums[fast]!=nums[fast-1]):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
