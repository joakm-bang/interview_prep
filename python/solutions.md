# Python fundamentals and binary search: Solutions

```python
from collections import defaultdict
import heapq
import math


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
    return [
        x
        for x, _ in heapq.nlargest(
            k, counts.items(), key=lambda item: item[1]
        )
    ]


def longest_consecutive(nums):
    values = set(nums)
    best = 0
    for x in values:
        if x - 1 not in values:
            y = x
            while y in values:
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


def binary_search(values, target):
    left, right = 0, len(values) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def lower_bound(values, target):
    """Return the first index i for which values[i] >= target."""
    left, right = 0, len(values)

    while left < right:
        mid = left + (right - left) // 2
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def minimum_capacity(package_sizes, max_batches):
    """Minimum capacity allowing sequential packages in at most max_batches."""
    if not package_sizes or max_batches <= 0:
        raise ValueError("package_sizes must be non-empty and max_batches positive")

    def batches_needed(capacity):
        batches = 1
        current = 0
        for size in package_sizes:
            if current + size > capacity:
                batches += 1
                current = 0
            current += size
        return batches

    left = max(package_sizes)
    right = sum(package_sizes)

    while left < right:
        mid = left + (right - left) // 2
        if batches_needed(mid) <= max_batches:
            right = mid
        else:
            left = mid + 1

    return left
```

Frequency counting is `O(n)` time and `O(k)` space for `k` distinct values. The consecutive-sequence solution is expected `O(n)`. Exact binary search and `lower_bound` are `O(log n)`. Binary search on the answer adds the cost of evaluating the feasibility predicate at each candidate capacity.
