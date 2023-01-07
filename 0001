class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums) # 数组长度
        for i in range(length):
            number2 = target - nums[i]
            flag = 0
            for j in range(length):
                if (number2==nums[j] and j!=i):
                    flag = 1
                    jj = j
            if (flag==1):
                list = [0, 0]
                list[0] = i
                list[1] = jj
                return list
