"""
This is a meeting room where you need to add to a min heap to see which room comes first and then count that
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        # Min heap to track end times
        heap = []

        for interval in intervals:
            # If a room is free, reuse it
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)

            # Allocate room
            heapq.heappush(heap, interval[1])

        return len(heap)