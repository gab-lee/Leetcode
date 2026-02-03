from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach
        Goal: remove overlapping ranges in a List of unsorted ranges
        sort list -> iterate and compare O(N) slow
        """
        intervals.sort(key=lambda x: x[0])
        merged_intervals=[intervals[0]]
    
        for i in range(1,len(intervals)):
            if intervals[i][0] <= merged_intervals[-1][1] and intervals[i][0] >= merged_intervals[-1][0]:
                if intervals[i][1] >= merged_intervals[-1][1]:
                    merged_intervals[-1] = [merged_intervals[-1][0],intervals[i][1]]
                else:
                    continue
            else:
                merged_intervals.append(intervals[i])
        
        return merged_intervals


if __name__ == "__main__":
    s = Solution()

    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))#[[1,6],[8,10],[15,18]]
    print(s.merge([[1,4],[4,5]]))#[[1,5]]
    print(s.merge([[4,7],[1,4]]))#[[1,7]]
    print(s.merge([[1,4],[1,4]]))#[[1,7]]
    print(s.merge([[1,4],[2,3]]))#[[1,4]]