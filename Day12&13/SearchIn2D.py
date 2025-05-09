class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        btm = len(matrix)-1

        while t<=btm:
            mid = (t+btm)//2

            if matrix[mid][0] < target and matrix[mid][-1]>target:
                break
            elif matrix[mid][0] > target:
                btm = mid -1
            else:
                t = mid +1

        row = (t+btm)//2
        l=0
        r=len(matrix[row]) -1 
        while l <=r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid]>target:
                r = mid-1
            else:
                l = mid+1

        return False