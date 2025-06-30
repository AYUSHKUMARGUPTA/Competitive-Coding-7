# LeetCode 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# Time Complexity: O(n log n) where n is the number of intervals -- O(n log n) for sorting and O(n log k) for heap operations
# where k is the number of rooms needed at any time.
# Space Complexity: O(n) for the heap
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        # Min-heap to track the end times of meetings
        heap = []
        heapq.heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            # If the room is free (meeting ended before next meeting starts), reuse it
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            
            # Push current meeting's end time
            heapq.heappush(heap, intervals[i][1])
        
        # Number of rooms needed is the size of the heap
        return len(heap)