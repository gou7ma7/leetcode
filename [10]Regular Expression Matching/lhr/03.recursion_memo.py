# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        is_match_map = [[0 for _ in range(p_len)] for _ in range(s_len)]

        def is_match(s_index, p_index):  # 为了递归求解，构造内部函数
            if p_index == p_len:  # p完了，看s是否匹配完了
                return s_index == s_len

            if s_index < s_len and is_match_map[s_index][p_index] is not 0:
                return is_match_map[s_index][p_index]

            now_match = s_index < s_len and p[p_index] in {s[s_index], '.'}

            if p_index < p_len - 1 and p[p_index + 1] == '*':  # p还剩2个以上字符，同时当前匹配的第二个字符为*，情况特殊单独讨论
                state = is_match(s_index, p_index + 2) or (now_match and is_match(s_index + 1, p_index))
                if s_index < s_len:
                    is_match_map[s_index][p_index] = state
                return state  # * 对应两种情况
            return is_match(s_index + 1, p_index + 1)

        return is_match(0, 0)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().isMatch('aa', 'a'))
    print(Solution().isMatch('aa', 'aa'))
    print(Solution().isMatch('aa', 'ab'))
    print(Solution().isMatch('aa', 'a*'))
    print(Solution().isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c'))
    print(Solution().isMatch('mississippi', 'mis*is*ip*.'))
