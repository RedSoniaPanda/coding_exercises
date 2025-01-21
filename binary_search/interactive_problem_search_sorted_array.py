def out_of_bound(value):
    return (2 ** 31 - 1) == value


class Solution:
    def search_2(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 1
        if out_of_bound(reader.get(right)):
            # Check if it's already out of bounds for quick return
            if reader.get(left) == target:  # Reduce api call by doing it here
                return left
            else:
                return -1

        while reader.get(right) < target:
            # Now we optimize the search space, by only changing the end
            # instead of both changing and taking more space
            right *= 2
        left = right // 2  # then after we optimized the right/end, we optimize the start

        # Now we begin the binary search
        while left <= right:
            mid = left + ((right - left) // 2)
            val = reader.get(mid)  # Reduce api call by doing it here
            if val == target:
                return mid

            if val > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1  # Always return this if we don't find a match

    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 1
        """ Sentinel value is a special val to indicate a specific condition/signal
        Serves as a marker for a limit/boundary/special case in an algorithm
        Chosen to be distinct from valid input vals
        Allows for boundary detection

        The problem says it'll return 2 ** 31 - 1 if the input to the api call
        doesn't exist in the array bounds. This is an example of a sentinel val.

        When designing - Can't be confused w/valid data, and must be consistent, and handled uniformly
        """

        # Solution number 1
        # Expand the range until the target is within bounds, or we hit out-of-bound values
        while reader.get(right) < target and reader.get(right) != 2**31 - 1:
            left = right
            right *= 2

        # Perform binary search within the determined bounds
        while left <= right:
            mid = left + (right - left) // 2
            value = reader.get(mid)

            if value == target:
                return mid
            elif value > target or value == 2**31 - 1:
                right = mid - 1
            else:
                left = mid + 1

        return -1


class ArrayReader:
    def __init__(self, array):
        self.array = array

    def get(self, num: int):
        # check index exists in array
        if num <= len(self.array) - 1:
            return self.array[num]
        else:
            return 2**31 - 1


def test_case_1():
    sol = Solution()
    reader = ArrayReader(array=[-1,0,3,5,9,12])
    target = 9
    expected = 4
    actual = sol.search(reader, target)
    assert actual == expected


def test_case_2():
    sol = Solution()
    reader = ArrayReader(array=[-1,0,3,5,9,12])
    target = 9
    expected = 4
    actual = sol.search_2(reader, target)
    assert actual == expected


if __name__ == "__main__":
    test_case_1()
    test_case_2()
