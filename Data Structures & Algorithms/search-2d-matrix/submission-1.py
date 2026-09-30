class Solution:
    def binarySearch(self, l: int, r: int, nums: List[int], target: int) -> bool:
        if l > r:
            return False

        m = l + (r - l) // 2

        if target == nums[m]:
            return True
        elif target > nums[m]:
            return self.binarySearch(m + 1, r, nums, target)
        
        return self.binarySearch(l, m - 1, nums, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                return self.binarySearch(0, len(row), row, target)
        
        return False