# Binary search

_An efficient search algorithm that finds a target in O(log n) time_

## Preconditions

**Monotonic (Sorted)**

- Binary search works when you can cut the search space in half based on a reliable direction.

Examples: sorted array/matrix

## Basic syntax

### Pitfalls

- Infinite loop prevention. Every iteration must strictly shrink the interval.

Key principle:
If mid is proven not the answer, it must be removed.

+1 and -1 — why they exist
low = mid + 1 → discard mid and everything left
high = mid - 1 → discard mid and everything right
They force progress because mid has already been checked.

## Types of searches

### Boundary Search

### Exact Search
