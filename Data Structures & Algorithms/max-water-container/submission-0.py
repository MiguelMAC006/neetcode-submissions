class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best, l , r = 0, 0, len(heights) - 1

        while l < r:
            length = r - l
            curr = min(heights[l], heights[r]) * length
            best = max(best, curr)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return best