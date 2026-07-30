class Solution:
    def numToBits(self, num: int) -> str:
        bitString = ""
        curNum = num

        while curNum > 0:
            remainder = curNum % 2

            if remainder == 1: bitString = "1" + bitString
            else: bitString = "0" + bitString
            curNum = curNum // 2
        
        while len(bitString) < 8:
            bitString = "0" + bitString
        
        return bitString
    
    def bitsToNum(self, bits: str) -> int:
        num = 0

        for j in range(len(bits)):
            if bits[j] == "1":
                num += 2 ** (7 - j)
        
        return num

    def encode(self, strs: List[str]) -> str:
        encoding = ""

        for string in strs:
            encoding += self.numToBits(len(string))
            encoding += string
        
        print(encoding)
        return encoding

    def decode(self, s: str) -> List[str]:
        decodedStrs = []

        i = 0
        while i < len(s):
            print(s[i:i+8])
            stringLen = self.bitsToNum(s[i:i+8])
            i += 8
            print(s[i:i+stringLen])
            decodedStrs.append(s[i:i+stringLen])
            i += stringLen
        
        return decodedStrs
