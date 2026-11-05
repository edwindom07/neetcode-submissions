class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] > target or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[r] < target or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
