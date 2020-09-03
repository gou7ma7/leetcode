from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        nums_dict = dict(zip(nums, list(range(len(nums)))))
        # print(nums)
        # print(nums_dict)
        result_list = []
        for left in range(nums_len - 1):
            if left and nums[left] == nums[left - 1]:
                continue
            for right in range(left + 1, nums_len):
                # print('left_index', left, nums[left], 'right_index', right, nums[right])
                if right > left + 1 and nums[right] == nums[right - 1]:
                    continue

                tow_sum = -(nums[left] + nums[right])
                tow_sum_index = nums_dict.get(tow_sum)
                if tow_sum_index and right < tow_sum_index:
                    # print('left_index', left, nums[left], 'right_index', right, nums[right], 'tow_sum_index', tow_sum_index, tow_sum)
                    result_list.append([nums[left], nums[right], tow_sum])

        return result_list


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().threeSum([0, 0, 0, 0]))
    print(Solution().threeSum([0, 0, 0]))
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

    # 解答成功:
    # 执行耗时: 1476 ms,击败了32.69% 的Python3用户
    # 内存消耗: 18MB, 击败了15.08 % 的Python3用户
