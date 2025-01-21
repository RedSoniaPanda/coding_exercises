from binary_tree.create_bst_ptrs import create_binary_tree, print_tree


class Solution:
    def closestValue(self, root, target) -> int:
        # Node values are from 0 - 10^9
        # target can be negative
        if target < 0:  # TODO write test case for when target is less than 0
            return -1

        closer = root
        curr_root = root

        while curr_root:
            if closer != curr_root:
                if abs(closer.val - target) == abs(curr_root.val - target):
                    mini = min(closer.val, curr_root.val)
                    if mini != closer.val:
                        closer = curr_root
                elif abs(closer.val - target) > abs(curr_root.val - target):
                    closer = curr_root

            # Go left or right based on target val
            if target < curr_root.val:
                curr_root = curr_root.left
            else:
                curr_root = curr_root.right

        return closer.val


def run_sol(arr, target, expected):
    root = create_binary_tree(arr)
    print('\n\n')
    print_tree(root)
    actual = Solution().closestValue(root, target)
    print("actual vs expected:")
    print(actual, expected)
    assert actual == expected


def test_case_1():
    arr = [4, 2, 5, 1, 3]
    target = 3.714286
    expected = 4
    run_sol(arr, target, expected)


def test_case_2():
    arr = [8]
    target = 3.714286
    expected = 8
    run_sol(arr, target, expected)


def test_case_3():
    arr = [8, 2]
    target = 3.714286
    expected = 2
    run_sol(arr, target, expected)


def test_case_4():
    arr = [8, None, 10]
    target = 3.714286
    expected = 8
    run_sol(arr, target, expected)


def test_case_5():
    arr = [8, 2, 9]
    target = -1
    expected = -1
    run_sol(arr, target, expected)


def test_case_6():
    arr = [2, 1, 3]
    target = 0.142857
    expected = 1
    run_sol(arr, target, expected)


def test_case_7():
    arr = [4, 2, 5, 1, 3]
    target = 3.5
    expected = 3
    run_sol(arr, target, expected)


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
