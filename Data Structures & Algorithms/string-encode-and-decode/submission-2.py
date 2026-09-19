class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)).rjust(3,'0'))
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        n = len(s)
        while index < n:
            j = int(s[index:index+3]) + 3
            res.append(s[index+3:index+j])
            index += j
        return res