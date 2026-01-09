class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 ==0:
            return -1 #odd numbers ending with 1 can't be divisible by 2 or 5
        else:
            remainder = 1
            for l in range(k):
                remainder = remainder % k
                if remainder == 0:
                    return l+1 #return len at which remainder %k==0
                remainder = (remainder*10 +1)% k #grow remainder 
                    
if __name__ == "__main__":
    s = Solution()

    print("Test case: Input =1")
    print(s.smallestRepunitDivByK(1))
    print("Test case: Input =2")
    print(s.smallestRepunitDivByK(2))
    print("Test case: Input =3")
    print(s.smallestRepunitDivByK(3))
    print("Test case: Input =5")
    print(s.smallestRepunitDivByK(5))
    print("Test case: Input =1311")
    print(s.smallestRepunitDivByK(127))
