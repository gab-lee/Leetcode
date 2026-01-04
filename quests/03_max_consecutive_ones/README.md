#[Q3. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i)

## Task

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

## Status: Completed

- Runtime: 15ms (70.19%)
- Memory: 20.01MB (68.24%)

## Approach

- Iterate through nums and store the positional value of 0 into a list
- compare the positional value and deduce the max consecutive 1
