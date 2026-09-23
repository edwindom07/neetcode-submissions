class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        l = 0
        maxf = 0
        unq = Counter()
        for r, c in enumerate(s):
            unq[c] += 1
            maxf = max(maxf, unq[c])

            while (r - l + 1) - maxf > k:
                unq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res