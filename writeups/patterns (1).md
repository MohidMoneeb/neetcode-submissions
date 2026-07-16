# Patterns I'm learning

Short notes to myself on the patterns behind the problems I've done, so I can *recognize* them
fast instead of re-deriving everything from scratch each time. I'll keep adding as I go.

## Hashing — the one I keep using

All three problems so far come down to the same move:
**a set or dict turns "have I seen this / where is this" from a scan into an instant lookup.**

Two shapes of it:

- **Set for membership** — "is this value already here?" That's Contains Duplicate exactly.
  O(1) to check, O(1) to add.
- **Dict for counting or matching** — store some info per value. Valid Anagram counts how many
  times each letter appears. Two Sum stores `value → index` so I can look up a complement.

The signal I watch for: if I catch myself writing a nested loop just to *find* or *match*
something, a hashmap usually kills the inner loop and takes it from O(n²) down to O(n). The cost
is O(n) extra memory, which is almost always worth it.

The gotcha I keep reminding myself: when I'm checking and inserting in the same loop,
**check before I insert**, or an element ends up matching itself.

## Coming up next

Patterns I haven't done yet but know are next, just so I recognize them when they show up:

- **Two pointers** — sorted array, walk in from both ends. Good for pair-sums on sorted data
  and palindrome checks.
- **Sliding window** — longest/shortest substring or subarray that satisfies some condition.
  Grow the window on the right, shrink from the left when it breaks the rule.
- **Stack** — matching brackets, "next greater element," anything that nests.

I'll write these up properly once I've actually solved a few and have my own take on them.
