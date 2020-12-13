class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            1.暴力 sort，sroted_str 相等？ O(NlogN)
            2.hash, map --> 统计每个字符的频次
        """
        if len(s) != len(t):
            return False
        table = {}
        for i in range(len(s)):
            if s[i] in table:
                table[s[i]] += 1
            else:
                table[s[i]] = 1
            if t[i] in table:
                table[t[i]] -= 1
            else:
                table[t[i]] = -1
        for v in table.values():
            if v:
                return False
        return True
