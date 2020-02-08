"""
56. Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
def merge_intervals(array):
    array.sort(key=lambda  x:x[0])
    merged=[]
    for item in array:
        if len(merged)==0:
            merged.append(item)
        else:
            if merged[-1][-1]>item[0]:
                merged[-1][1]=item[-1]
            else:
                merged.append(item)
    return merged
print(merge_intervals([[21,31],[2,6],[5,10],[2,18]]))