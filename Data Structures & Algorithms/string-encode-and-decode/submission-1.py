class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [str(len(strs)).rjust(3,'0')]
        for s in strs:
            res.append(str(len(s)).rjust(3,'0'))
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        index = 3
        n = int(s[0:3])
        print(s)
        for i in range(n):
            j = int(s[index:index+3]) + 3
            res.append(s[index+3:index+j])
            index += j
        return res