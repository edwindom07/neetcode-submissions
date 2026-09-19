class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            if d.get(num) != None:
                return [d.get(num), idx]
            d[target - num] = idx
        return []