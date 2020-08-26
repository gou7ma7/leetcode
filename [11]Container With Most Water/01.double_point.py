from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        if right < 1:
            return 0

        max_area = min(height[0], height[1])
        while left < right:
            # print(left, height[left], right, height[right])
            max_area = max((right - left) * min(height[left], height[right]), max_area)
            # if max_area == 16:
            # print(left, right)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]))
    print(Solution().maxArea([1, 1]))
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))