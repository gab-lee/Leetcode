# [Q3. Palindrome Number](https://leetcode.com/problems/palindrome-number/description/?envType=problem-list-v2&envId=maths-m1-arithmetic-basic-reasoning)

## Task

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?

## Status:

- Runtime: 36ms (5.30%)
- Memory: 19.63MB (13.65%)

## Approach (without converting into a string)

- ~~I believe there is a rule where 11 can be used to check if something is pallindrome -> every even length pallindrome in base 10 is divisible by 11.~~ Necessary but not sufficient condition.
- reject if n is negative.
- I can iterate through the size of the number and check first and last number.
