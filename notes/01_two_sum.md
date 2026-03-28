# Two Sum 

## Related Leetcode questions
- [**0001 Two Sum**](https://github.com/gab-lee/Leetcode/tree/main/problems/0001_two_sum): unsorted array, return indices
- [**0167 Two Sum II**](https://github.com/gab-lee/Leetcode/tree/main/problems/0167_two_sum_II_input_array_is_sorted): sorted array, return indices (1-indexed)
- **0170 Two Sum III**: design a data structure for add/find operations
- **0653 Two Sum IV**: Two sum in binary search tree
- [**0015 3Sum**](https://github.com/gab-lee/Leetcode/tree/main/problems/0015_3sum): find all unique triplets that sum to 0
- **0016 3Sum closest**: find triplet closest to target 
- **0259 3Sum Smaller**:count triplets with sum less than target
- **0018 4Sum**: find all unique quadruplets that sum to target
- **0454 4Sum II**: four arrays, count combinations


## Problem Concept
Find all combinations of K numbers from an array that sum to a target value.

**Challenge:** Doing this efficiently while handling duplicates.

## What This Tests
- **Search strategy** — brute force (checking all combinations) is O(n^K), which is too slow
- **Using constraints** — exploiting structure (sorting, hashing) to prune the search space
- **Deduplication** — avoiding redundant combinations when values repeat

## Core Techniques

**1. Two Pointers (when sorted)**
- Move left/right pointers based on sum comparison
- Skip duplicates by comparing adjacent values (only applicable when there is >1 possible solution)
- Time: O(n), Space: O(1)
- **Use for:** 2Sum II, 3Sum, 4Sum

**2. Hash Map (when unsorted)**
- Store seen values for O(1) lookup
- Time: O(n), Space: O(n)
- **Use for:** 2Sum I

**3. Fix + Reduce Pattern**
- Fix one element, solve (K-1)-Sum on the rest
- 3Sum = fix one → 2Sum
- 4Sum = fix one → 3Sum
- Recursively reduces until you hit 2Sum base case

## General K-Sum Template (Sorted Array)
1. Sort the array
2. Loop through, fixing first element
   - Skip duplicates: `if i > 0 && nums[i] == nums[i-1]: continue`
3. Recursively solve (K-1)-Sum on remaining elements
4. Base case (2Sum): use two pointers

## Handling Duplicates
- **In sorted arrays:** Compare with previous element (`nums[i] == nums[i-1]`)
- **After finding a match:** Advance pointers past duplicate values