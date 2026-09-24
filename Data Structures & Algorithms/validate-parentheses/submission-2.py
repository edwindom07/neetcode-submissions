class Solution:
    def isValid(self, s: str) -> bool:
        # only 6 chars
        stack = [] # use only append and pop
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(ord(c)+1+(ord(c)%2))
            elif not stack or stack.pop() != ord(c):
                return False
        return True if not stack else False