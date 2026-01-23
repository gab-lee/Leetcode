class Solution:
    def reverseBits(self, n: int) -> int:
        #convert n to bits 
        bit = []
        while n > 0:
            bit.append(n%2)
            n = n//2
        
        bit = bit + [0]*(32-len(bit))
        inverse = 0

        #calcualate inverse bit
        #print(bit)
        for i in range(len(bit)):
            inverse += bit[i] * (2**(32-i-1))
         
        return inverse
        
if __name__ == "__main__":
    s = Solution()

    print(s.reverseBits(8)) #8
    print(s.reverseBits(43261596)) #964176192
    print(s.reverseBits(2147483644)) #1073741822
