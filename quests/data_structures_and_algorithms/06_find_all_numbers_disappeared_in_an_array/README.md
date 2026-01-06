# [Q3. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii)

## Task

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

## Status:

- Runtime: 47ms (22.72%)
- Memory: 35.82MB (16.33%)

## Approach

- Create a dict with all expected keys. Iterate through nums, and if key is present, add the value.
- ~~Reverse the dict. Iterate through dict and create list for values if False. //I think this takes up a lot of space~~
- Turns out I might not even need to reverse the dict.
- A faster way would be to mark the positions of numbers that exists. positions that are not marked would then be of the missin numbers.
