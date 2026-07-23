# Sliding windows: Solutions

```python
from collections import Counter, defaultdict

def max_window_sum(a, k):
    if not 1 <= k <= len(a):
        raise ValueError("invalid k")
    cur = best = sum(a[:k])
    for r in range(k, len(a)):
        cur += a[r] - a[r-k]
        best = max(best, cur)
    return best

def moving_averages(a, k):
    cur = sum(a[:k])
    out = [cur / k]
    for r in range(k, len(a)):
        cur += a[r] - a[r-k]
        out.append(cur / k)
    return out

def min_subarray_len(target, nums):
    left = cur = 0
    best = float("inf")
    for right, x in enumerate(nums):
        cur += x
        while cur >= target:
            best = min(best, right-left+1)
            cur -= nums[left]
            left += 1
    return 0 if best == float("inf") else best

def longest_unique_substring(s):
    last, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right-left+1)
    return best

def longest_at_most_k_distinct(s, k):
    counts = defaultdict(int)
    left = best = 0
    for right, ch in enumerate(s):
        counts[ch] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        best = max(best, right-left+1)
    return best

def min_window(s, t):
    if not t:
        return ""
    need, have = Counter(t), defaultdict(int)
    required, formed, left = len(need), 0, 0
    best = (float("inf"), None, None)
    for right, ch in enumerate(s):
        have[ch] += 1
        if ch in need and have[ch] == need[ch]:
            formed += 1
        while formed == required:
            if right-left+1 < best[0]:
                best = (right-left+1, left, right)
            c = s[left]
            have[c] -= 1
            if c in need and have[c] < need[c]:
                formed -= 1
            left += 1
    return "" if best[1] is None else s[best[1]:best[2]+1]

def count_product_lt_k(nums, k):
    if k <= 1:
        return 0
    product, left, total = 1, 0, 0
    for right, x in enumerate(nums):
        product *= x
        while product >= k:
            product /= nums[left]
            left += 1
        total += right-left+1
    return total
```
