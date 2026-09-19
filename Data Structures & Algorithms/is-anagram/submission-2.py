class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #chars = [None for _ in range(26)]
        return Counter(s) == Counter(t)