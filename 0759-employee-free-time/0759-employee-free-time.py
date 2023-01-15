"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        result = []
        intervals=[y for x in schedule for y in x]
        intervals.sort(key=lambda x:x.start)

        maxEnd=intervals[0].end
        for interval in intervals:
            if interval.start>maxEnd:
                empty=Interval(maxEnd,interval.start)
                result.append(empty)
        
            maxEnd=max(maxEnd,interval.end)
            
        return result