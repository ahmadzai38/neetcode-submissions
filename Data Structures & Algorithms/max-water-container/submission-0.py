class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_Area = 0
        l , r = 0 , len(heights)-1
        while l<r:
            area = (r - l) * min(heights[l], heights[r])
            max_Area = max(max_Area, area)
            if heights[l]<heights[r]:
                l += 1
            else:
                r -= 1
        return max_Area 