"""
# Definition for a Node.
"""
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p

        return p1


def create_binary_tree(values):
    if not values:
        return None

    # Create the root node
    root = Node(values[0])
    queue = [root]  # Use a queue to manage nodes in level-order
    i = 1  # Index to traverse the input list

    while queue and i < len(values):
        current = queue.pop(0)

        # Assign left child
        if i < len(values) and values[i] is not None:
            current.left = Node(values[i])
            current.left.parent = current  # Set parent
            queue.append(current.left)
        i += 1

        # Assign right child
        if i < len(values) and values[i] is not None:
            current.right = Node(values[i])
            current.right.parent = current  # Set parent
            queue.append(current.right)
        i += 1

    return root


def print_tree(root):
    if not root:
        print("Tree is empty")
        return

    print("Printing tree:")
    # Use a queue for level-order traversal
    queue = deque([(root, 0)])  # (node, level)
    current_level = 0
    result = ""

    while queue:
        node, level = queue.popleft()

        # Start a new level
        if level != current_level:
            result += "\n"
            current_level = level

        # Print the current node value
        result += f"{node.val if node else 'None'} "

        # Add child nodes to the queue
        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

    print(result)
    print('\n')


def test_case_1():
    values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_binary_tree(values)
    print_tree(root)
    p_node = root.left
    q_node = root.right
    sol = Solution()
    result = sol.lowestCommonAncestor(p_node, q_node)
    if result is not None:
        print(f"LCA of {p_node.val} and {q_node.val} is {result.val}")
        assert result.val == 3
    else:
        print("LCA is None test case 1")


def test_case_2():
    values = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_binary_tree(values)
    print_tree(root)
    p_node = root.left
    q_node = root.left.right.right
    sol = Solution()
    result = sol.lowestCommonAncestor(p_node, q_node)
    assert None != result
    print(f"LCA of {p_node.val} and {q_node.val} is {result.val}")
    assert result.val == 5


if __name__ == '__main__':
    # Example usage:
    test_case_1()
    test_case_2()
