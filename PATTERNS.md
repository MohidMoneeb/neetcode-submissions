# Patterns Cheat Sheet

The night-before-interview skim. Each pattern: **when to reach for it**, the **core idea**, a
**minimal template**, **complexity**, the **one gotcha**, and **problems that drill it**.

Read order for building intuition: Arrays & Hashing → Two Pointers → Sliding Window → Stack →
Binary Search → Linked List → Trees → Tries → Heap → Backtracking → Graphs → Advanced Graphs →
1-D DP → 2-D DP → Greedy → Intervals → Math & Bit.

---

## 1. Arrays & Hashing

**Trigger** — "have I seen this before?", counting frequencies, finding a complement, or
de-duping. Anytime a nested loop is doing repeated lookups, a hash map collapses it.

**Core idea** — trade space for time: one pass building a dict/set, one pass (or the same pass)
querying it in O(1).

```python
# complement one-pass (Two Sum shape)
seen = {}                       # value -> index
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i

# frequency count
from collections import Counter
freq = Counter(nums)            # {value: count}
```

**Complexity** — O(n) time, O(n) space.

**Gotcha** — insert into the map *after* checking, or you'll match an element with itself.

**Drills** — Two Sum, Group Anagrams, Top K Frequent Elements, Valid Anagram, Contains
Duplicate, Product of Array Except Self, Longest Consecutive Sequence.

---

## 2. Two Pointers

**Trigger** — a **sorted** array (or one you can sort), palindrome checks, or pairing from both
ends. If brute force is comparing all pairs on sorted data, two pointers is O(n).

**Core idea** — one pointer at each end; move the one that can improve the answer.

```python
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s == target: return [l, r]
    elif s < target: l += 1     # need bigger -> move left up
    else: r -= 1                # need smaller -> move right down
```

**Complexity** — O(n) time (O(n log n) if you sort first), O(1) space.

**Gotcha** — sorting destroys original indices; if the problem wants indices, capture them
before sorting or use a hash map instead.

**Drills** — Valid Palindrome, Two Sum II, 3Sum, Container With Most Water, Trapping Rain Water.

---

## 3. Sliding Window

**Trigger** — "longest / shortest / max / min substring or subarray satisfying X." Contiguous
range + a running condition.

**Core idea** — expand `right` to grow the window; shrink `left` while the window is invalid.
Maintain window state incrementally instead of recomputing.

```python
# variable-size window
left = 0
state = {}                      # or a counter / running sum
best = 0
for right, x in enumerate(s):
    # add s[right] to state
    while window_invalid(state):
        # remove s[left] from state
        left += 1
    best = max(best, right - left + 1)
return best
```

**Complexity** — O(n) time (each element enters/leaves once), O(k) space for window state.

**Gotcha** — the shrink condition. Off-by-one here is the classic bug: decide whether the
window includes `right` before you measure its size.

**Drills** — Longest Substring Without Repeating Characters, Longest Repeating Character
Replacement, Minimum Window Substring, Best Time to Buy/Sell Stock, Permutation in String.

---

## 4. Stack

**Trigger** — matching/nesting (parentheses), "next greater/smaller element", or you need to
undo/backtrack the most recent thing. Monotonic stacks handle the "next greater" family.

**Core idea** — LIFO. Push context; pop when the current element resolves what's on top.

```python
# monotonic (increasing) stack: next greater element
stack = []                      # holds indices
res = [-1] * len(nums)
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        res[stack.pop()] = x    # x is the next greater for that index
    stack.append(i)
```

**Complexity** — O(n) time (each index pushed/popped once), O(n) space.

**Gotcha** — decide whether the stack holds values or indices *up front*; you usually need
indices to compute distances/spans.

**Drills** — Valid Parentheses, Min Stack, Daily Temperatures, Car Fleet, Largest Rectangle
in Histogram, Generate Parentheses, Evaluate Reverse Polish Notation.

---

## 5. Binary Search

**Trigger** — a sorted array, OR a monotonic answer space ("smallest X such that condition
holds"). If you can phrase it as "is X feasible?" and feasibility is monotonic, binary search
*on the answer*.

**Core idea** — halve the search space each step by testing the midpoint.

```python
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: lo = mid + 1
    else: hi = mid - 1
return -1

# binary search on answer: min capacity/speed/etc.
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid): hi = mid
    else: lo = mid + 1
return lo
```

**Complexity** — O(log n) time, O(1) space.

**Gotcha** — the loop invariant. Pick `<=` with `mid±1`, OR `<` with `hi=mid`, and don't mix
them. Infinite loops come from `lo = mid` without a `+1`.

**Drills** — Binary Search, Search a 2D Matrix, Koko Eating Bananas, Find Minimum in Rotated
Sorted Array, Search in Rotated Sorted Array, Time Based Key-Value Store, Median of Two Sorted
Arrays.

---

## 6. Linked List

**Trigger** — anything with `next` pointers: reversal, cycle detection, middle-finding, merging.

**Core idea** — two techniques cover most of it: **fast/slow pointers** (cycles, middle) and a
**dummy head** (clean insert/delete at the front).

```python
# reverse a list
prev = None
cur = head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
return prev

# fast/slow: detect cycle
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
    if slow is fast: return True
return False
```

**Complexity** — O(n) time, O(1) space.

**Gotcha** — save `cur.next` before you overwrite it, or you lose the rest of the list. Use a
dummy node whenever the head itself might change.

**Drills** — Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle, Reorder List,
Remove Nth Node From End, Copy List with Random Pointer, Add Two Numbers, LRU Cache, Merge K
Sorted Lists.

---

## 7. Trees

**Trigger** — anything hierarchical. DFS (recursion) for path/depth/structure questions; BFS
(queue) for level-order or shortest-depth.

**Core idea** — recursion mirrors the tree's shape. Ask: what do I return from a node given its
children's answers?

```python
# DFS
def dfs(node):
    if not node: return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)

# BFS level order
from collections import deque
q = deque([root])
while q:
    for _ in range(len(q)):     # one full level
        node = q.popleft()
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
```

**Complexity** — O(n) time; space O(h) for DFS recursion (h = height), O(w) for BFS (w = max
width).

**Gotcha** — the null base case, and remembering BST order gives you sorted traversal (use it
to validate/search in O(h)).

**Drills** — Invert Binary Tree, Max Depth, Diameter, Balanced Binary Tree, Same Tree, Subtree,
LCA of BST, Level Order Traversal, Validate BST, Kth Smallest in BST, Construct Tree from
Preorder/Inorder, Serialize/Deserialize, Binary Tree Max Path Sum.

---

## 8. Tries

**Trigger** — prefix queries, autocomplete, word dictionaries, "does any word start with…".

**Core idea** — a tree keyed by character; each node maps a char to a child, with an end-of-word
flag.

```python
class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.end = False

def insert(root, word):
    node = root
    for ch in word:
        node = node.children.setdefault(ch, TrieNode())
    node.end = True
```

**Complexity** — insert/search O(L) where L = word length; space O(total chars inserted).

**Gotcha** — distinguish "word exists" (`end` flag) from "prefix exists" (node reachable).

**Drills** — Implement Trie, Design Add and Search Words (wildcard `.` → DFS over children),
Word Search II (trie + grid backtracking).

---

## 9. Heap / Priority Queue

**Trigger** — "top K", "K largest/smallest", "median of a stream", repeatedly grabbing the
min/max, or merging sorted sources.

**Core idea** — a heap gives O(log n) push/pop with O(1) peek at the extreme. Python's `heapq`
is a min-heap; negate values for a max-heap.

```python
import heapq
# K largest: keep a min-heap of size k
heap = []
for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > k:
        heapq.heappop(heap)     # evict smallest -> heap holds k largest
return heap[0]                  # kth largest
```

**Complexity** — building O(n), each op O(log n); top-K in O(n log k).

**Gotcha** — for "K largest" use a **min**-heap of size k (evict the smallest), not a max-heap;
it keeps the pass O(n log k) instead of O(n log n).

**Drills** — Kth Largest Element in a Stream, Last Stone Weight, K Closest Points to Origin,
Kth Largest Element in Array, Task Scheduler, Design Twitter, Find Median from Data Stream (two
heaps).

---

## 10. Backtracking

**Trigger** — "generate all", subsets, permutations, combinations, or constraint satisfaction
(N-Queens, Sudoku). Exponential output → you're exploring a decision tree.

**Core idea** — choose → recurse → **undo the choice**. The undo is what makes it backtracking.

```python
def backtrack(start, path):
    res.append(path[:])         # record current subset (copy!)
    for i in range(start, len(nums)):
        path.append(nums[i])    # choose
        backtrack(i + 1, path)  # explore
        path.pop()              # un-choose
```

**Complexity** — subsets O(n·2ⁿ), permutations O(n·n!). Space O(n) recursion depth.

**Gotcha** — append a **copy** (`path[:]`) when recording, and match `start`/`i+1` to whether
reuse is allowed (combinations vs. combination-sum-with-reuse).

**Drills** — Subsets, Combination Sum, Permutations, Subsets II, Combination Sum II, Word
Search, Palindrome Partitioning, Letter Combinations, N-Queens.

---

## 11. Graphs

**Trigger** — grids, networks, "connected components", "can you reach", "shortest path in
unweighted graph". Islands and matrices are graphs in disguise.

**Core idea** — DFS or BFS over nodes, tracking `visited`. BFS gives shortest path when edges
are unweighted. Union-Find when you're merging groups.

```python
# BFS on a grid (shortest path / flood fill)
from collections import deque
def bfs(start):
    q = deque([start])
    visited = {start}
    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if in_bounds(nr,nc) and (nr,nc) not in visited and grid[nr][nc]==1:
                visited.add((nr,nc))
                q.append((nr,nc))

# Union-Find
parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # path compression
        x = parent[x]
    return x
def union(a, b): parent[find(a)] = find(b)
```

**Complexity** — DFS/BFS O(V + E); Union-Find near O(1) amortized per op with path compression.

**Gotcha** — mark visited *when you enqueue*, not when you dequeue, or nodes get added twice.

**Drills** — Number of Islands, Clone Graph, Max Area of Island, Pacific Atlantic Water Flow,
Surrounded Regions, Rotting Oranges, Course Schedule, Graph Valid Tree, Number of Connected
Components, Redundant Connection, Word Ladder.

---

## 12. Advanced Graphs

**Trigger** — **weighted** shortest path, dependency ordering, minimum spanning tree, or "cheapest
route with K stops".

**Core idea** — Dijkstra (heap-based, non-negative weights), topological sort (Kahn's / DFS on a
DAG), Prim/Kruskal for MST, Bellman-Ford for K-stop / negative edges.

```python
# Dijkstra
import heapq
dist = {start: 0}
pq = [(0, start)]
while pq:
    d, node = heapq.heappop(pq)
    if d > dist.get(node, float('inf')): continue
    for nei, w in graph[node]:
        nd = d + w
        if nd < dist.get(nei, float('inf')):
            dist[nei] = nd
            heapq.heappush(pq, (nd, nei))

# Topological sort (Kahn's)
from collections import deque
q = deque([n for n in nodes if indegree[n] == 0])
order = []
while q:
    n = q.popleft(); order.append(n)
    for nei in graph[n]:
        indegree[nei] -= 1
        if indegree[nei] == 0: q.append(nei)
# len(order) < num_nodes  ->  cycle exists
```

**Complexity** — Dijkstra O(E log V); topo sort O(V + E); Kruskal O(E log E).

**Gotcha** — Dijkstra breaks with negative weights (use Bellman-Ford). For topo sort, a leftover
node count < total means there's a cycle.

**Drills** — Network Delay Time, Cheapest Flights Within K Stops, Reconstruct Itinerary, Min Cost
to Connect All Points, Swim in Rising Water, Alien Dictionary.

---

## 13. 1-D Dynamic Programming

**Trigger** — "how many ways", "min/max cost to reach", overlapping subproblems along a single
axis. Fibonacci-shaped recurrences.

**Core idea** — define `dp[i]` in terms of earlier states, then either memoize top-down or fill
bottom-up. Often reducible to O(1) rolling variables.

```python
# house robber shape: dp[i] = max(skip, take)
prev, cur = 0, 0
for x in nums:
    prev, cur = cur, max(cur, prev + x)
return cur
```

**Complexity** — O(n) time; O(1) space once you roll the array into a couple of variables.

**Gotcha** — nail the recurrence and base cases on paper first. Most 1-D DP bugs are a wrong
transition, not a coding error.

**Drills** — Climbing Stairs, House Robber, House Robber II, Coin Change, Longest Increasing
Subsequence, Word Break, Decode Ways, Maximum Product Subarray, Partition Equal Subset Sum.

---

## 14. 2-D Dynamic Programming

**Trigger** — two changing dimensions: two strings (edit distance, LCS), a grid, or
weight×items (knapsack).

**Core idea** — `dp[i][j]` depends on neighbors (`i-1`, `j-1`). Fill row by row; often
compressible to one or two rows.

```python
# grid unique paths
dp = [[1]*n for _ in range(m)]
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
return dp[m-1][n-1]
```

**Complexity** — O(m·n) time; O(m·n) space, often reducible to O(n).

**Gotcha** — get the table dimensions and boundary row/column right; +1 sizing for
string-DP (empty-prefix base case) trips people constantly.

**Drills** — Unique Paths, Longest Common Subsequence, Edit Distance, Coin Change II, Target Sum,
Interleaving String, Longest Increasing Path in Matrix, Distinct Subsequences, Burst Balloons.

---

## 15. Greedy

**Trigger** — "maximum profit / minimum count" where a **locally** optimal choice provably leads
to a global optimum. Often involves sorting first.

**Core idea** — make the best immediate choice and never reconsider. Correctness needs an
exchange/argument, not just intuition — prove it or you'll be wrong on adversarial cases.

```python
# jump game: track furthest reachable index
reach = 0
for i, jump in enumerate(nums):
    if i > reach: return False
    reach = max(reach, i + jump)
return True
```

**Complexity** — usually O(n log n) (sorting) or O(n).

**Gotcha** — greedy is *often wrong*. If a counterexample exists, it's a DP problem in disguise.
Sanity-check on a small adversarial input before committing.

**Drills** — Maximum Subarray, Jump Game, Jump Game II, Gas Station, Hand of Straights, Merge
Triplets to Form Target, Partition Labels, Valid Parenthesis String.

---

## 16. Intervals

**Trigger** — lists of `[start, end]` pairs: merging, overlaps, scheduling, "minimum rooms".

**Core idea** — sort by start (sometimes by end), then sweep left to right comparing each
interval to the last kept one.

```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:              # overlap
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
return merged
```

**Complexity** — O(n log n) for the sort, O(n) sweep.

**Gotcha** — decide whether touching endpoints (`start == prev_end`) count as overlapping; it
changes the `<` vs `<=` and flips answers.

**Drills** — Insert Interval, Merge Intervals, Non-overlapping Intervals, Meeting Rooms, Meeting
Rooms II, Minimum Interval to Include Each Query.

---

## 17. Math & Bit Manipulation

**Trigger** — no-extra-space constraints, powers of two, XOR tricks, digit manipulation, or
"do it without `+`/`*`".

**Core idea** — bit ops are O(1) tools: XOR cancels pairs, `n & (n-1)` clears the lowest set
bit, `n & 1` tests parity.

```python
# single number: XOR cancels every pair, leaves the unique
res = 0
for x in nums:
    res ^= x
return res

# count set bits
count = 0
while n:
    n &= n - 1                  # drop lowest set bit
    count += 1
```

**Complexity** — typically O(n) or O(number of bits), O(1) space.

**Gotcha** — Python ints are arbitrary-precision; when a problem assumes 32-bit, mask with
`& 0xFFFFFFFF` and handle the sign yourself.

**Drills** — Single Number, Number of 1 Bits, Counting Bits, Reverse Bits, Missing Number, Sum of
Two Integers, Reverse Integer, Plus One, Pow(x, n), Multiply Strings.

---

## Fast diagnosis: input signal → pattern

| You see… | Reach for… |
|---|---|
| "seen before?", frequency, complement | Arrays & Hashing |
| sorted array, palindrome, pair from ends | Two Pointers |
| longest/shortest contiguous sub-thing | Sliding Window |
| nesting, next greater, undo recent | Stack |
| sorted, or "min X such that feasible" | Binary Search |
| `next` pointers, cycle, middle | Linked List |
| hierarchical, path, depth, level | Trees |
| prefix, autocomplete, dictionary | Tries |
| top-K, median stream, repeated min/max | Heap |
| generate all, subsets, permutations | Backtracking |
| grid, connected, reach, unweighted path | Graphs (BFS/DFS/Union-Find) |
| weighted path, ordering, MST | Advanced Graphs |
| ways/min-cost along one axis | 1-D DP |
| two strings, grid, knapsack | 2-D DP |
| local choice → global optimum | Greedy |
| `[start, end]` pairs | Intervals |
| powers of two, XOR, no extra space | Math & Bit |
