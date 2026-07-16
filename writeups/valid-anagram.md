# Valid Anagram

Easy · Arrays & Hashing · [problem](https://neetcode.io/problems/is-anagram) · [my submission](../Data%20Structures%20%26%20Algorithms/is-anagram/submission-1.py)

**The problem:** given two strings `s` and `t`, return `true` if `t` is an anagram of `s`
(same letters, same counts, just reordered).

## How I thought about it

My first instinct was the cheap trick: if two strings are anagrams, then sorting both gives
the exact same string. So `sorted(s) == sorted(t)` and you're done. It passes, and for an easy
problem I won't pretend that's a bad answer.

But sorting is O(n log n), and the "real" interview answer is counting. Two strings are
anagrams exactly when every character shows up the same number of times in each. So I built a
frequency dictionary for both strings and compared them. I also put a length check at the top:
if the two lengths differ, they can't be anagrams, so I return early before counting anything.

The `.get(char, 0)` bit is just "the current count, or 0 if I haven't seen this character yet,"
so I can `+ 1` without a KeyError.

## First version (works, but slower)

```python
return sorted(s) == sorted(t)
```

## Version I'd actually submit

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
```

## Complexity

- **Sorting version:** O(n log n) time.
- **Counting version:** O(n) time. Space is O(1) if you treat the alphabet as fixed (26 lowercase
  letters), or O(n) in the general case.

Trade I'm making: the counting version costs a bit of memory for the two dicts but gets me from
O(n log n) down to O(n).

---

> ### 1-minute revision
> - **When you see it:** "rearrangement / same characters / anagram" → count letters.
> - **Idea:** build a frequency map of each string and compare. (Sort-both is the quick fallback.)
> - **Gotcha:** check lengths first. And `Counter(s) == Counter(t)` does the whole thing in one line.
> - **Skeleton:**
> ```python
> from collections import Counter
> return Counter(s) == Counter(t)
> ```
