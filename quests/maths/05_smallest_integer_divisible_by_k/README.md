# [Q2. Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k/description/?envType=problem-list-v2&envId=maths-m2-divisibility-modular-arithmetic)

## Task

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.

Constraints:

1 <= k <= 105

## Status:

- Runtime: 0ms (100%)
- Memory: 19.26MB (16.01%)

## Approach (without converting into a string)

- n for n%k == 0 and n is only contains 1 and is > 0.
