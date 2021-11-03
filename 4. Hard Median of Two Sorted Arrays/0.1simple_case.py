from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_small = nums2_small = 0
        nums1_big = len(nums1) - 1
        nums2_big = len(nums2) - 1

        while nums1_big - nums1_small + nums2_big - nums2_small > 2:
            break
            # TODO

        # 只剩下其中一个列表
        if nums1_small > nums1_big:
            return (nums2[nums2_small] + nums2[nums2_big]) / 2
        if nums2_small > nums2_big:
            return (nums1[nums1_small] + nums1[nums1_big]) / 2

        return (max(nums1[nums1_small], nums2[nums2_small]) + min(nums1[nums1_big], nums2[nums2_big])) / 2


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([0, 1, 2], [100, 101]))  # 1.5
    # print(Solution().findMedianSortedArrays([2], []))
    # print(Solution().findMedianSortedArrays([], [1]))
    # print(Solution().findMedianSortedArrays([0, 0], [0, 0]))
    # print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
    # print(Solution().findMedianSortedArrays([1, 3], [2]))
