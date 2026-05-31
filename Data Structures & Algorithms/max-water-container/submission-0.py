class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxvol = 0
        while left < right :
            vol = (right-left) * min(heights[left],heights[right])
            maxvol = max (vol,maxvol)
            if heights[left] < heights[right]:
                left = left + 1
            else :
                right = right -1
        return maxvol
