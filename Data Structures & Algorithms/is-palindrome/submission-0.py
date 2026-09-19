class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(clean) - 1
        
        while left < right:
            if clean[left] != clean[right]:
                print(clean[left], clean[right])
                return False
            left += 1
            right -= 1
        
        return True