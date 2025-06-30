# Time Complexity: O(n*log(max-min)) n is the number of rows and columns
# Space Complexity: O(1)
# Binary Search Solution
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[-1][-1]

        def countLessEqual(mid):
            count = 0
            row = n - 1
            col = 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low


# Time Complexity: O(n^2 * log(k)) n is the number of rows and columns
# Space Complexity: O(k)
# Heap Solution
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []
        for row in matrix:
            for val in row:
                heapq.heappush(max_heap, -val)  # Use negative to simulate max-heap
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
        return -max_heap[0]