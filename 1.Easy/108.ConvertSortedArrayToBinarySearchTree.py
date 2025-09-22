class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            node = TreeNode(arr[mid])
            node.left = dfs(arr[:mid])
            node.right = dfs(arr[mid+1:])
            return node
        return dfs(nums)
