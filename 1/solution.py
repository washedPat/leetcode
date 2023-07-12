from typing import List
"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [2, 11, 7, 15]
        target = 9

        dict = {
            2: 0,
            11: 1,


        }

        9 - 2 -> not in map

        9 - 11 -> not in map

        9 - 7 -> in map -> return [0, 2]

        """
        indexTable = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexTable:
                return [indexTable[diff], i]
            else:
                indexTable[nums[i]] = i

        return []
        


def compare_arrays(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    if compare_arrays(solution.twoSum(nums, target), [0,1]):
        print("Example 1: Pass")
    else:
        print("Example 1: Fail")


    nums = [3,2,4]
    target = 6

    if compare_arrays(solution.twoSum(nums, target), [1,2]):
        print("Example 2: Pass")
    else:
        print("Example 2: Fail")


    nums = [3,3]
    target = 6

    if compare_arrays(solution.twoSum(nums, target), [0,1]):
        print("Example 3: Pass")
    else:
        print("Example 3: Fail")

    
    nums = [100, 200]
    target = 0

    if compare_arrays(solution.twoSum(nums, target), []):
        print("Example 4: Pass")
    else:
        print("Example 4: Fail")
