# Two Sum

Easy · Arrays & Hashing · [problem](https://neetcode.io/problems/two-integer-sum) · [my submission](../Data%20Structures%20%26%20Algorithms/two-integer-sum/submission-2.py)

**The problem:** given an array `nums` and a `target`, return the indices of the two numbers
that add up to `target`. Exactly one valid answer is guaranteed.

## How I thought about it

My first version was the obvious one: a double loop that checks every pair. If
`nums[i] + nums[j] == target`, return `[i, j]`. It's easy to reason about and I got it working
fast, but it's O(n²) and I knew there was a better way.

The key realization: for any number `n`, the number I actually need is fixed. It's
`target - n`, the complement. So instead of scanning for it, I can remember what I've already
seen in a hashmap and look the complement up in O(1). I stored `value → index`, then walked the
array checking whether each number's complement was in the map, with a guard so a number
doesn't pair with itself.

## Brute force (my first attempt)

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

## Hashmap version (what I submitted)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # value -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
```

## One thing I'd tighten up

My version does two passes and builds the whole dict first. That means if the array has
duplicate values, the dict only keeps the *last* index of each. It still works here because the
problem guarantees exactly one answer, but the cleaner approach is a **single pass** that checks
for the complement *before* inserting the current number. That way I never store something I
don't need, and the "don't match yourself" case is handled for free:

```python
seen = {}
for i, n in enumerate(nums):
    if target - n in seen:
        return [seen[target - n], i]
    seen[n] = i
```

## Complexity

- **Brute force:** O(n²) time, O(1) space.
- **Hashmap:** O(n) time, O(n) space.

That's the trade — I spend memory on the map to get rid of the nested loop.

---

> ### 1-minute revision
> - **When you see it:** "find two things that add to X" → hashmap of complements.
> - **Idea:** for each `n`, the thing you need is `target - n`. Store seen values, look up the complement.
> - **Gotcha:** check for the complement *before* inserting the current number — handles the "self-match" and duplicate cases cleanly.
> - **Skeleton:**
> ```python
> seen = {}
> for i, n in enumerate(nums):
>     if target - n in seen:
>         return [seen[target - n], i]
>     seen[n] = i
> ```
