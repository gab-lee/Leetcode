from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Exactly one solution, two elements will definitely return [1,2] 
        Ignore if number is too small or too big 
        """
        l = len(numbers)
        hasNeg = False
        if numbers[0] <0:
            hasNeg = True
        for i in range(l-1,-1,-1):
            #remove out of range 
            print(numbers[i])
            if hasNeg and numbers[0]+ numbers[i] > target: 
                continue #number out of range 
            elif not hasNeg and numbers[i] > target: 
                continue #number out of range
            
            for j in range (i):
                print(f"{numbers[i]}+{numbers[j]}")
                if numbers[i]+numbers[j] == target:
                    return [j+1,i+1]
        

if __name__ == "__main__":
    s = Solution()

    print(s.twoSum([2,7,11,15],9)) #[1,2]
    print(s.twoSum([2,3,4],6)) #[1,3]
    print(s.twoSum([-1,0],-1)) #[1,2]