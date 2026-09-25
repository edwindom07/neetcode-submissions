class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append((val, min(val, self.s[len(self.s)-1][1] if self.s else val+1)))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[len(self.s)-1][0]

    def getMin(self) -> int:
        return self.s[len(self.s)-1][1]
