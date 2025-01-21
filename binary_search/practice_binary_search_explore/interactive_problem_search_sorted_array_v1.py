from binary_search.interactive_problem_search_sorted_array import ArrayReader

class Solution:
    def search(self, reader, target) -> int:
        l, r = 0, 1
        while reader.get(r) < target and reader.get(r) != (2**31 - 1):
            l += 1
            r *= 2

        while l <= r:
            mid = l + (r - l) // 2
            val = reader.get(mid)
            if val == target:
                return mid

            if target < val and val != 2**31 - 1:
                r = mid - 1
            else:
                l = mid + 1

        return -1


def run_test(reader, target, expected):
    sol = Solution()
    actual = sol.search(reader, target)
    assert actual == expected


def test_case_1():
    reader = ArrayReader(array=[-1,0,3,5,9,12])
    target = 9
    expected = 4
    run_test(reader, target, expected)


if __name__ == "__main__":
    test_case_1()
