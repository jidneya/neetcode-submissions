class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        subarray = -1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                subarray = mid
                break
            elif target >= matrix[mid][-1]:
                l = mid + 1
            elif target <= matrix[mid][0]:
                r = mid - 1
        if subarray == -1:
            return False
        l,r = 0, len(matrix[subarray])-1
        while l <= r:
            mid = (l+r)//2
            if target == matrix[subarray][mid]:
                return True
            elif target < matrix[subarray][mid]:
                r = mid-1
            else:
                l = mid+1
        return False
        