class MinStack:
    """
    A stack that keeps track of the lowest value
    """
    def __init__(self):
        self.s = []
        self.min = []

    def push(self, val: int) -> None:
        self.s.append(val)
        self.min.append(min(val, self.min[len(self.min)-1]if self.min else val+1))

    def pop(self) -> None:
        self.s.pop()
        self.min.pop()

    def top(self) -> int:
        return self.s[len(self.s)-1]

    def getMin(self) -> int:
        return self.min[len(self.min)-1]

        
