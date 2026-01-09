# [Q1. Ugly Number](https://leetcode.com/problems/ugly-number/description/?envType=problem-list-v2&envId=maths-m2-divisibility-modular-arithmetic)

## Task

An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:

-231 <= n <= 231 - 1

## Status:

- Runtime: 0ms (100%)
- Memory: 19.26MB (16.01%)

## Approach (without converting into a string)

- Straightforward while loop, return False if n can't be divisible by 2,3,5.
  //could have been better whereby I check after each loop, but I don't know if it would make a huge difference.
