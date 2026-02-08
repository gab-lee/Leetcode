class Solution:
    def countMonobit(self, n: int) -> int:
        """
        Monobit must be 1(1),11(3),111(7),1111(15)
        I can check the counts of 1 
        """
        monobits = 1 #keep track of the number of monobits
        count = 0 

        #initial case
        if n == count:
            return monobits
        while True:
            temp = count + 2 ** (monobits-1)
            if temp > n:
                return monobits 
            count = temp
            monobits +=1 
        return monobits
        
if __name__ == "__main__":
    s = Solution()

    print(s.countMonobit(0)) #1
    print(s.countMonobit(1)) #2
    print(s.countMonobit(3)) #3
    print(s.countMonobit(4)) #3
    print(s.countMonobit(16)) #5
