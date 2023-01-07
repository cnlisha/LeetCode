class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0):
            return False
        else:
            list = [int(a) for a in str(x)] # 转化为数字数组
            length = len(list)
            for i in range(length):
                if (list[i]!=list[length-i-1]):
                    return False
            return True
