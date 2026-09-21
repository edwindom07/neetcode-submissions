class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1
        1
        2
        1
        0,1
        l = 0
        Lmax = 2
        r = 1
        Rmax = 3
        res = 3 + 2 + (2) = 6
        
        """
        if len(height) < 2:
            return 0
        
        res = 0
        l, r = 0, len(height) - 1
        lMax = height[l]
        rMax = height[r]
        while l < r:
            if lMax < rMax:
                l+=1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r-=1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res