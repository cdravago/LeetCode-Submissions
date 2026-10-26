class MinStack:

    def __init__(self):
        self.s = []

    def push(self, value: int) -> None:
        current_min = min(value, self.s[-1][1]) if self.s else value
        self.s.append((value, current_min))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()