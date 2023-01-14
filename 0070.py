class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        stairs = [0]*(n+1)
        stairs[0] = 1
        stairs[1] = 2
        for i in range(2,n+1):
            stairs[i] = stairs[i-1] + stairs[i-2]

        if (n==1):
            return 1
        elif (n==2):
            return 2
        else:
            return stairs[i-1]
