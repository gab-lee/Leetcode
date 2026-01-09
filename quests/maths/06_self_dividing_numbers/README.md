# [Q3. Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/description/?envType=problem-list-v2&envId=maths-m2-divisibility-modular-arithmetic)

## Task

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]

Constraints:

1 <= left <= right <= 104

## Status: Completed

- Runtime: 10ms (38.09%)
- Memory: 19.42MB (8.11%)

## Approach (without converting into a string)

- iterate through the nums
- iterate through the digits of the num, stopping if the num can't be divided by a certain num
- 1 can definitely be divided, 0 can't be divided.
