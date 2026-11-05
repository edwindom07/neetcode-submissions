class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]
        
        """
        binary search, 
            if l > r, answer in right side,
            if mid 
        """

        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] <= nums[r] or r - l == 1:
                break
            mid = (r - l) // 2 + l

            if nums[mid] < nums[l]:
                r = mid
                continue
            
            if nums[r] < nums[mid]:
                l = mid
        
        return min(nums[l], nums[r])