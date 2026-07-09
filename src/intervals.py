def merge_intervals(intervals):
    """Merge overlapping intervals into the smallest set of non-overlapping
    intervals, sorted by start. Touching intervals ([1,3],[3,5]) merge.
    Each interval is a [start, end] pair with start <= end.
    """
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda pair: pair[0])
    merged = [list(ordered[0])]
    for start, end in ordered[1:]:
        last = merged[-1]
        if start <= last[1]:
            # BUG: overwrites the end instead of extending it, so a nested
            # interval like [2,3] inside [1,5] wrongly shrinks the merge to [1,3].
            last[1] = end
        else:
            merged.append([start, end])
    return merged
