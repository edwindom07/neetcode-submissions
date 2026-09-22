class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = [None for _ in range(95)]
        res = 0
        l = 0
        for r in range(len(s)):
            x = ord(s[r])-32
            if cur[x]!=None:
                l = max(cur[x]+1, l)
            cur[x] = r
            res = max(res, r - l + 1)

        return res