class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = s.split()
        word_num = len(str)
        return (len(str[word_num-1]))
