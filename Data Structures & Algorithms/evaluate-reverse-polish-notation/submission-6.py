import math

class Solution:
    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x - y
    
    def mul(self, x, y):
        return x * y
    
    def div(self, x, y):
        result = x / y

        if result > 0: return math.floor(result)
        
        return math.ceil(result)

    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []

        opDict = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div
        }

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                secondNum = numStack.pop(len(numStack) - 1)
                firstNum = numStack.pop(len(numStack) - 1)
                numStack.append(opDict[token](firstNum, secondNum))
            else:
                numStack.append(int(token))
            print(numStack)
            
        return numStack.pop(len(numStack) - 1)