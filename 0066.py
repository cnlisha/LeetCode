class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 将数字数组转化为十进制数
        num = 0
        for digit in digits:
            num = num*10 + digit
        
        num += 1
        digits = [int(i) for i in str(num)]

        return digits
