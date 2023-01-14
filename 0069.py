class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 二分法
        if (x<=1):
            return x
        else:
            min = 0
            max = x
            while (max-min>1):
                mid = int((max+min)/2)   
                if (mid>x/mid):
                    max = mid
                else:
                    min = mid
            return int(min)
