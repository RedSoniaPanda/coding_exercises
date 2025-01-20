# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/
from typing import List


class Solution:
    def find_start_point(self, arr, x):
        left = 0
        n = len(arr) - 1
        right = n

        while left < right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return mid

            if left == 0 and arr[left] > x:
                return left
            elif right == n and arr[right] < x:
                return right
            if (abs(arr[left] - x) < abs(arr[right] - x)) or ((abs(arr[left] - x) == abs(arr[right] - x)) and (arr[left] < x)):
                right -= 1
            else:
                left += 1
        return right

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = self.find_start_point(arr, x) - 1
        right = left + 1
        while right - left - 1 < k:
            if left < 0:
                # Don't go over left bound
                right += 1
                continue
            if (right == len(arr)) or (abs(arr[left] - x) < abs(arr[right] - x)) or ((abs(arr[left] - x) == abs(arr[right] - x)) and (arr[left] < x)):
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]

    # BAD SOLUTION
    # def find_start_point(self, arr, x):
    #     left = 0
    #     n = len(arr) - 1
    #     right = n
    #
    #     while left <= right:
    #         mid = (left + right) // 2
    #
    #         if arr[mid] == x:
    #             return mid
    #         if mid < 0 or mid > n:
    #             return -1
    #         if arr[mid] < x:
    #             right += 1
    #         else:
    #             left -= 1
    #     return -1
    #
    # def find_closest_x(self, arr, x, l, r, stop_left, stop_right):
    #     if stop_left:
    #         return r
    #     elif stop_right:
    #         return l
    #     if x - arr[l] == arr[r] - x:
    #         # They're equally distant, picking left
    #         return l
    #     elif (abs(arr[l] - x) < abs(arr[r] - x)) or ((abs(arr[l] - x) == abs(arr[r] - x)) and (arr[l] < x)):
    #         return l
    #     else:
    #         return r
    #
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     """x doesn't have to be in arr
    #     Determine mid-point which will be left + (right - left) // 2? N - should be (left + right) // 2
    #     if (abs(a - x) < abs(b - x)) or ((abs(a - x) == abs(b - x)) and (a < x)) - add `a` to the output list
    #     I'm thinking the if condition should be checked after getting numbers that are close to x?
    #     Or does it make more sense that the if condition would determine which way to search.
    #     Probably search for a pivot point first? then I should find the min distance from x to it's neighbors"""
    #     if k == 0 or len(arr) == 0:
    #         return []
    #     if len(arr) <= k:
    #         return arr
    #
    #     start_point = self.find_start_point(arr, x)
    #     output = []
    #     n = len(arr) - 1
    #     if start_point != -1:
    #         output.append(arr[start_point])
    #     if start_point == 0:
    #         # grab k from right
    #         output = arr[k - 1:]
    #         return output
    #     if start_point == n:
    #         # grab k from left
    #         output = arr[:k]
    #         return output
    #
    #     # find the closest element to x on the left
    #     stop_left = False
    #     stop_right = False
    #     if start_point != -1:
    #         l = start_point - 1
    #         r = start_point + 1
    #         while (l != -1 and r != n + 1) or (len(output) != k):
    #             # x is in the array so it should have neighbors
    #             closest = self.find_closest_x(arr, x, l, r, stop_left, stop_right)
    #             output.append(arr[closest])
    #             if closest == l:
    #                 l -= 1
    #             else:
    #                 r += 1
    #             if l == -1:
    #                 stop_left = True
    #             if r == n + 1:
    #                 stop_right = True
    #     else:
    #         l = 0
    #         r = n
    #         mid = l + r // 2
    #         closest = self.find_closest_x(arr, x, mid - 1, mid + 1, stop_left, stop_right)
    #         while (l != -1 and r != n + 1) or (len(output) != k):
    #             mid = l + r // 2
    #
    #             if closest == l and closest == r:
    #                 closest_left = self.find_closest_x(arr, x, l, mid, stop_left, stop_right)
    #                 closest_right = self.find_closest_x(arr, x, mid, r, stop_left, stop_right)
    #                 closest = self.find_closest_x(arr, x, closest_left, closest_right, stop_left, stop_right)
    #             if closest == mid - 1:
    #                 closest = self.find_closest_x(arr, x, l, mid, stop_left, stop_right)
    #             else:
    #                 closest = self.find_closest_x(arr, x, mid, r, stop_left, stop_right)
    #
    #             if closest == l:
    #                 l -= 1
    #             else:
    #                 r += 1
    #             if l == -1:
    #                 stop_left = True
    #             if r == n + 1:
    #                 stop_right = True
    #
    #             output.append(arr[closest])
    #
    #     return output



def find_closest_elem(arr, k, x):
    sol = Solution()
    return sol.findClosestElements(arr, k, x)


def test_case_1():
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    expected = [1, 2, 3, 4]
    actual = find_closest_elem(arr, k, x)
    assert actual == expected


def test_case_2():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 4
    x = 5
    expected = [4, 5, 6, 7]
    actual = find_closest_elem(arr, k, x)
    assert actual == expected or actual == [3, 4, 5, 6]


def test_case_3():
    arr = [1, 1, 2, 3, 4, 5]
    k = 4
    x = -1
    expected = [1, 1, 2, 3]
    actual = find_closest_elem(arr, k, x)
    assert actual == expected


def test_case_4():
    arr = [1, 1, 2, 3, 4, 5, 6]
    k = 4
    x = 4
    expected = [2, 3, 4, 5]
    actual = find_closest_elem(arr, k, x)
    assert actual == expected


def test_case_5():
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 5
    expected = [2, 3, 4, 5]
    actual = find_closest_elem(arr, k, x)
    assert actual == expected


def test_case_6():
    arr = [1,1,1,10,10,10]
    k = 1
    x = 9
    expected = [10]
    actual = find_closest_elem(arr, k, x)
    assert actual == expected



if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
