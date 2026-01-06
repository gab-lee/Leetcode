class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = ((n*(n+1))//2)** 0.5
        ans = int(pivot) if pivot.is_integer() else -1
        return ans

if __name__ == "__main__":
    s = Solution()

    print(s.pivotInteger(8))
    print(s.pivotInteger(1))
    print(s.pivotInteger(4))