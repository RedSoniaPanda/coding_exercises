from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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
            # current.left.parent = current  # Set parent
            queue.append(current.left)
        i += 1

        # Assign right child
        if i < len(values) and values[i] is not None:
            current.right = Node(values[i])
            # current.right.parent = current  # Set parent
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
    values = [4, 2, 5, 1, 3]
    root = create_binary_tree(values)
    print_tree(root)


if __name__ == "__main__":
    test_case_1()
