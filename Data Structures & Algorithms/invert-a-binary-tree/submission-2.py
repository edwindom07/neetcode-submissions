# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def has_children(node: Optional[TreeNode]) -> bool:
            return node.right or node.left
        if not root or not has_children(root):
            return root
        def swap_children(node: Optional[TreeNode]) -> None:
            node.right, node.left = node.left, node.right

        swap_children(root)

        st = []
        if root.right:
            st.append(root.right)
        if root.left:
            st.append(root.left)

        while st:
            cur = st.pop()
            if has_children(cur):
                swap_children(cur)
                if cur.right:
                    st.append(cur.right)
                if cur.left:
                    st.append(cur.left)
        return root