# Contains Duplicate

Easy · Arrays & Hashing · [problem](https://neetcode.io/problems/duplicate-integer) · [my submission](../Data%20Structures%20%26%20Algorithms/duplicate-integer/submission-1.py)

**The problem:** given an array of integers, return `true` if any value appears more than once.

## How I thought about it

"Appears more than once" is really the question *"have I seen this number before?"* asked
once for every element. That's a lookup, and the fastest structure for repeated lookups is a
set, since checking membership is O(1) on average.

So the plan is one pass: for each number, check if it's already in the set. If it is, there's
my duplicate, return `True` immediately. Otherwise add it and keep going.

I also thought about the lazy one-liner `return len(set(nums)) != len(nums)`. It works, but it
always builds the whole set before comparing lengths. The loop version is nicer because it can
bail the moment it finds the first repeat instead of processing the rest of the array.

## My solution

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
```

## Complexity

- **Time:** O(n) — single pass, and each set lookup/insert is O(1) on average.
- **Space:** O(n) — worst case every element is unique and ends up in the set.

---

> ### 1-minute revision
> - **When you see it:** "any duplicates?" / "seen before?" → reach for a set.
> - **Idea:** one pass, check membership before inserting.
> - **Gotcha:** check *first*, then add — otherwise a number matches itself.
> - **Skeleton:**
> ```python
> seen = set()
> for n in nums:
>     if n in seen:
>         return True
>     seen.add(n)
> return False
> ```
