class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            out.append(root.val)
            traverse(root.right)

        traverse(root)

        return out
