# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs on both trees
        if not p:
            return not q
        if not q:
            return False
        
        d = deque()
        d.append((p,q))

        while d:
            for _ in range(len(d)):
                node1, node2 = d.popleft()
                if node1.val != node2.val:
                    return False
                if node1.right and node2.right:
                    d.append((node1.right, node2.right))
                elif node1.right or node2.right:
                    return False
                if node1.left and node2.left:
                    d.append((node1.left, node2.left))
                elif node1.left or node2.left:
                    return False
        return True