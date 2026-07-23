# Python fundamentals: Solutions

```python
from collections import defaultdict
import heapq, math

def frequency_table(values):
    out = {}
    for x in values:
        out[x] = out.get(x, 0) + 1
    return out

def first_unique_index(s):
    counts = frequency_table(s)
    return next((i for i, ch in enumerate(s) if counts[ch] == 1), -1)

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())

def top_k_frequent(values, k):
    counts = frequency_table(values)
    return [x for x, _ in heapq.nlargest(k, counts.items(), key=lambda kv: kv[1])]

def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:
            y = x
            while y in s:
                y += 1
            best = max(best, y - x)
    return best

def robust_mean(values):
    clean = []
    for value in values:
        if value is None:
            continue
        try:
            x = float(value)
        except (TypeError, ValueError):
            continue
        if math.isfinite(x):
            clean.append(x)
    return None if not clean else sum(clean) / len(clean)
```

Frequency counting is `O(n)` time and `O(k)` space for `k` distinct values. The consecutive-sequence solution is expected `O(n)`.
