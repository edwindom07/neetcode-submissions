class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        product = 1
        for num in nums:
            if num:
                product *= num
            else:
                zero += 1
        if zero > 1:
            return [0] * len(nums)
        res = []
        if zero == 1:
            for num in nums:
                if not num:
                    res.append(product)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(product//num)
        return res