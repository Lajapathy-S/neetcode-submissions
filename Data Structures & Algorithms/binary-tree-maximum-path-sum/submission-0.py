class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # global max tracker

        def dfs(node):
            if not node:
                return 0

            # get max gain from left and right children
            # if negative, ignore it (take 0 instead)
            left_gain  = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # path through this node (left + node + right)
            path_sum = node.val + left_gain + right_gain

            # update global max
            self.max_sum = max(self.max_sum, path_sum)

            # return only ONE side to parent (can't go both ways up)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum