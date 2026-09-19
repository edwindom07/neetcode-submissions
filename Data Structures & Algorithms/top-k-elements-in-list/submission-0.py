class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()
        for num in nums:
            c[num] += 1
        return [i[0] for i in c.most_common(k)]