class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        left, right = 0, len(height)-1
        while left < right:
            result = max(result, min(height[left], height[right]) * (right-left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result

a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))
print(a.maxArea([1,2,1]))
