class Solution:
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

        # Expand the range until the target is within bounds, or we hit out-of-bound values
        while reader.get(right) < target and reader.get(right) != 2 ** 31 - 1:
            left = right
            right *= 2

        # Perform binary search within the determined bounds
        while left <= right:
            mid = left + (right - left) // 2
            value = reader.get(mid)

            if value == target:
                return mid
            elif value > target or value == 2 ** 31 - 1:
                right = mid - 1
            else:
                left = mid + 1

        return -1
