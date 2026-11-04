class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        
        countT, window = Counter(t), Counter()

        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = len(s) + 1

        l = 0
        for r, c in enumerate(s):
            window[c] += 1
            have += 1 if 0 != countT[c] == window[c] else 0
        
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r + 1]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                have -= 1 if 0 != countT[s[l]] > window[s[l]] else 0
                l += 1
        
        l, r = res
        return s[l:r] if resLen <= len(s) else ""