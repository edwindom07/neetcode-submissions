class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        chars = []
        for string in strs:
            tmp = [0 for _ in range(26)]
            for char in string:
                tmp[ord(char) - 97] += 1
            tmp = tuple(tmp)
            if d.get(tmp) != None:
                res[d.get(tmp)].append(string)
            else:
                d[tmp] = len(res)
                res.append([string])
        return res