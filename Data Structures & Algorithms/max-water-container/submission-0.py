class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:
            shorter = min(heights[left], heights[right])
            curr_area = (right - left) * shorter
            maximum = max(curr_area, maximum)
            if shorter == heights[left]:
                left += 1
            else:
                right -= 1
        return maximum