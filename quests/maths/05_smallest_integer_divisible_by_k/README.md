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

## Status: Completed

- Runtime: 14ms (35.21%)
- Memory: 19.37MB (20.67%)

## Approach (without converting into a string)
```
- return -1 if k is even or if k is a multiple of 5. 
- n for n%k == 0 and n is only contains 1 and is > 0.
- remainders will repeat. 
|-- remainder for %5 is 1 and that keeps repeating
|-- remainder for %3 is 1,2,0
|-- remainder for %7 is 1,4,6
|-- Pigeonhole principle, %7 can only have 7 outcomes [0,1,2,3,4,5,6]
- ~~grow n each iteration~~ Apparently thi`s takes up a lot of time/memory
|-- Instead: grow the remainder `remainder = (remainder*10 + 1) % k`
- Proof
|-- Rn+1 ​= 10 Rn​+1 
|-- remainder_n = Rn % k
|-- Rn+1 **% k** ​= 10 Rn​+1 **% k** //add %k to both sides
|-- remainder_n+1 ​= 10 remainder_n **% k** //add %k to both sides 
```