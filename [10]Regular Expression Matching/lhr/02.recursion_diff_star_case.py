# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        def is_match(s_index, p_index):  # 为了递归求解，构造内部函数
            if p_index == p_len:  # p完了，看s是否匹配完了
                return s_index == s_len

            now_match = (s_index < s_len and p[p_index] in {s[s_index], '.'})

            if p_index < p_len - 1 and p[p_index + 1] == '*':  # p还剩2个以上字符，同时当前匹配的第二个字符为*，情况特殊单独讨论
                return is_match(s_index, p_index + 2) or (now_match and is_match(s_index + 1, p_index))  # * 对应两种情况

            return now_match and is_match(s_index + 1, p_index + 1)

        return is_match(0, 0)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().isMatch('mississippi', 'mis*is*ip*.'))
    print(Solution().isMatch('aa', 'a*'))
    print(Solution().isMatch('aa', 'a'))
    print(Solution().isMatch('aa', 'aa'))
    print(Solution().isMatch('aa', 'ab'))