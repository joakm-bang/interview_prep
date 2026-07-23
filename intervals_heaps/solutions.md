# Intervals, scheduling, and heaps: Solutions

```python
import heapq

def merge_intervals(intervals, merge_touching=True):
    if not intervals:
        return []
    intervals = sorted(intervals)
    out = [list(intervals[0])]
    for start, end in intervals[1:]:
        overlap = start <= out[-1][1] if merge_touching else start < out[-1][1]
        if overlap:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return [tuple(x) for x in out]

def idle_days(days, sessions):
    clipped = [(max(1,s), min(days,e)) for s,e in sessions if max(1,s) <= min(days,e)]
    busy = sum(e-s+1 for s,e in merge_intervals(clipped))
    return days - busy

def min_meeting_rooms(intervals):
    heap = []
    for start, end in sorted(intervals):
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)

def insert_interval(intervals, new):
    result, i = [], 0
    start, end = new
    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i]); i += 1
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0]); end = max(end, intervals[i][1]); i += 1
    return result + [(start,end)] + intervals[i:]

class RunningMedian:
    def __init__(self):
        self.low, self.high = [], []
    def add(self, x):
        heapq.heappush(self.low, -x)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    def median(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2

def gas_station(gas, cost):
    total = tank = start = 0
    for i, (g,c) in enumerate(zip(gas,cost)):
        total += g-c; tank += g-c
        if tank < 0:
            start, tank = i+1, 0
    return start if total >= 0 else -1
```

If the running tank goes negative at `i`, no starting point since the previous reset can reach `i+1`, so all are discarded.
