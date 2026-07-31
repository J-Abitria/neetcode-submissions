class Solution:
    def isValid(self, s: str) -> bool:
        opStack = []

        for symbol in s:
            if symbol == '(' or symbol == '[' or symbol == '{':
                opStack.append(symbol)
            else:
                if len(opStack) == 0: return False

                if symbol == ')' and opStack[len(opStack) - 1] == '(':
                    opStack.pop(len(opStack) - 1)
                elif symbol == ']' and opStack[len(opStack) - 1] == '[':
                    opStack.pop(len(opStack) - 1)
                elif symbol == '}' and opStack[len(opStack) - 1] == '{':
                    opStack.pop(len(opStack) - 1)
                else:
                    return False
        
        return len(opStack) == 0