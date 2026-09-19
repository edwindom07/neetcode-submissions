class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        streak = 0
        cur = 0
        isStreak = False
        numSet = set(nums)
        for num in numSet:
            if num-1 not in numSet:
                # this is the start of a subsequence
                cur = num + 1
                streak += 1
                while cur in numSet:
                    streak += 1
                    cur += 1
                res = max(res, streak)
                streak = 0
        return res