import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x//10 == 0:
            return True
        else: 
            size = int(math.log10(x)+1)
            print (size)
            for i in range(size):
                back = (x % 10 ** (i+1))//(10**i)
                front = x//(10**(size-i-1))%10
                #print("num:",x,"back:",back,"front:",front)
                if (back == front):
                    continue
                else:
                    return False
            return True

if __name__ == "__main__":
    s = Solution()

    print(s.isPalindrome(1000021))
    print(s.isPalindrome(0))
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))