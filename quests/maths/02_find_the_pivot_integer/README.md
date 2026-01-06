# [Q2. Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer/description/?envType=problem-list-v2&envId=maths-m1-arithmetic-basic-reasoning)

## Task

Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.

Constraints:

1 <= n <= 1000

## Status:

- Runtime: 0ms (100%)
- Memory: 19.60MB (12.71%)

## Approach

- sum of 1 to x = x(x+1)//2.
- sum of x to n = n(n+1)//2 - x(x-1)//2
- pivot number is when
  x(x+1)//2 == n(n+1)//2 - x(x-1)//2
  x(x+1)+x(x-1) == n(n+1)
  x[(x+1)+(x-1)] == n(n+1)
  2x^2 == n(n+1)
  x == sqrt (n(n+1) // 2)
