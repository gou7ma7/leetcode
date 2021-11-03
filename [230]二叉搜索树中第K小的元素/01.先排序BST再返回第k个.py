from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ordered_list2bst(val_list):
    root = TreeNode(val_list[0])

    for i in val_list[1:]:
        if i:
            add_bst_node(root, i)
    return root


def add_bst_node(node: TreeNode, val):
    if val < node.val:
        if node.left:
            add_bst_node(node.left, val)
        else:
            node.left = TreeNode(val)
    else:
        if node.right:
            add_bst_node(node.right, val)
        else:
            node.right = TreeNode(val)


class Solution:

    def bst2ordered_list(self, root: TreeNode):
        result = []
        self.visit_bst(root, result)
        return result

    def visit_bst(self, node: TreeNode, result):
        if node.left:
            self.visit_bst(node.left, result)
        result.append(node.val)
        if node.right:
            self.visit_bst(node.right, result)
        # if not node.left and not node.right:
        #     result.append(None)

    # def pop_smallest_node(self, node):
    #     if val < node.val:
    #         if node.left:
    #             return self.find_bigger_val(node.left, val)
    #         else:
    #             return node.val if node.val > val else val
    #     else:
    #         if node.right:
    #             return self.find_bigger_val(node.right, val)
    #         else:
    #             return node.val if val < node.val else val

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        return self.bst2ordered_list(root)[k - 1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root_node = ordered_list2bst([5, 3, 6, 2, 4, None, None, 1])
    print(Solution().kthSmallest(root_node, 3))  # out: 3

# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#
#
#  示例 2：
#
#
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
