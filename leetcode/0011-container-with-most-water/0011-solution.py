class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0
        while left < right:
            height_left = height[left]
            height_right = height[right]
            
            maxarea = max(maxarea, (right - left) * min(height_left, height_right))
            if height_left < height_right:
                while left < right and height[left] <= height_left:
                    left += 1
            else:
                while left < right and height[right] <= height_right:
                    right -= 1
        return maxarea
