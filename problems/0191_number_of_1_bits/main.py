class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        while n > 0:
            #print(n)
            hw += n%2
            n = n // 2
        return hw

        
if __name__ == "__main__":
    s = Solution()

    print(s.hammingWeight(11))
    print(s.hammingWeight(128))
    print(s.hammingWeight(2147483645))
    print(s.hammingWeight(1))