class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array is sorted, we just need to keep track of one sum
        x = 0
        y = len(numbers) - 1
        while x < y:
            if numbers[x] + numbers[y] == target:
                return [x+1, y+1]
            if numbers[y] + numbers[x] > target:
                y -= 1
            else:
                x += 1
        return []