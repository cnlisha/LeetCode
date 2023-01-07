class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace("IV", "a") # 4
        s = s.replace("IX", "b") # 9
        s = s.replace("XL", "c") # 40
        s = s.replace("XC", "d") # 90
        s = s.replace("CD", "e") # 400
        s = s.replace("CM", "f") # 900

        num = 0
        for i in range(len(s)):
            if (s[i]=="I"):
                num += 1
            if (s[i]=="V"):
                num += 5
            if (s[i]=="X"):
                num += 10
            if (s[i]=="L"):
                num += 50
            if (s[i]=="C"):
                num += 100
            if (s[i]=="D"):
                num += 500
            if (s[i]=="M"):
                num += 1000

            if (s[i]=="a"):
                num += 4
            if (s[i]=="b"):
                num += 9
            if (s[i]=="c"):
                num += 40
            if (s[i]=="d"):
                num += 90
            if (s[i]=="e"):
                num += 400
            if (s[i]=="f"):
                num += 900

        return num
