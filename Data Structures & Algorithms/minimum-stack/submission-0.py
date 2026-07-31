class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.stack) == 1:
            self.minVal.append(val)
        else:
            self.minVal.append(min(self.minVal[len(self.minVal) - 1], val))
        

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop(len(self.stack) - 1)
            self.minVal.pop(len(self.minVal) - 1)
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.minVal[len(self.stack) - 1]
        
