class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min_len = 100 # 最短单词长度
        for i in range(len(strs)):
            if (len(strs[i])<min_len):
                min_len = len(strs[i])
        
        output = ""
        for i in range(min_len):
            flag = 0
            for j in range(len(strs)-1):
                if (strs[j][i]!=strs[j+1][i]):
                    flag = 1
            if (flag==0): # 均一致
                output = output + strs[0][i]
            else:
                return output
        
        return output
