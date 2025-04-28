class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(p, q):
            if not p or not q:
                return p == q
            
            if not traverse(p.left, q.left):
                return False
            if p.val != q.val:
                return False
            if not traverse(p.right, q.right):
                return False

            return True

        return traverse(p, q)
