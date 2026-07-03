class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0

        for i,h in enumerate(heights):
            r = i+1
            while r < len(heights) and heights[r] >= h:
                r+=1
            r -= 1
            l = i
            while l >=0 and heights[l] >= h:
                l-=1
            l+=1
            area = max(area, h*(r-l+1))
        return area
            


