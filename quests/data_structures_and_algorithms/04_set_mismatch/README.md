# [Q4. Set Mismatch](https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii)

## Task

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104

## Status: Completed

- Runtime: 9ms (69.64%)
- Memory: 19.06 (54.82%)

## Approach

- ~~Sort the list and set a comparator as the first element of the list.~~
- ~~Iterate nums, storing the old number, and comparing it with the current number.~~
- Iterate through nums and used a hash table to store unique occurence of numbers.
- If iterated value is found in set, store it as duplicate.
- Find the missing number by calculating the correct value of 1-n and minusing the sum of seen values.
- Removed nums.sorted -> unnecessary step.

//Despite completing it, the performance of the code seems to fall behind others.
