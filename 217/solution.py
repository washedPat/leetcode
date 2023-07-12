from typing import List
"""
217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for e in nums:
            if e in numDict:
                return True
            else:
                numDict[e] = 0
        return False

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,1]
    if solution.containsDuplicate(nums) == True:
        print("Example 1: Pass")
    else:
        print("Example 1: Fail")
        
    nums = [1,2,3,4]
    if solution.containsDuplicate(nums) == False:
        print("Example 2: Pass")
    else:
        print("Example 2: Fail")

    nums = [1,1,1,3,3,4,3,2,4,2]
    if solution.containsDuplicate(nums) == True:
        print("Example 3: Pass")
    else:
        print("Example 3: Fail")
