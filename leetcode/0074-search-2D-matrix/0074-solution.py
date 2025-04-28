class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m * n - 1

        while lo < hi - 1:
            mid = int((lo + hi) / 2)
            if matrix[int(mid / n)][mid % n] < target:
                lo = mid
            else:
                hi = mid

        if matrix[int(lo / n)][lo % n] == target or matrix[int(hi / n)][hi % n] == target:
            return True
        else:
            return False
