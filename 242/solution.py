"""
242: Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from typing import Dict


class Solution:
    def create_histogram(self, s: str) -> Dict[str, int]:
        histogram = {}
        for c in s:
            if c in histogram:
                histogram[c] += 1
            else:
                histogram[c] = 1
        return histogram

    def compare_historgrams(self, s: Dict[str, int], t: Dict[str, int]) -> bool:
        for k,v in s.items():
            if k not in t:
                return False
            if t[k] != v:
                return False
        return True



    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hist = self.create_histogram(s)
        t_hist = self.create_histogram(t)

        for k,v in s_hist.items():
            if k not in t_hist:
                return False
            if t_hist[k] != v:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    s = "anagram"
    t = "nagaram"

    if solution.isAnagram(s,t) == True:
        print("Example 1: Pass")
    else:
        print("Example 1: Fail")

    s = "rat"
    t = "car"
    if solution.isAnagram(s, t) == False:
        print("Example 2: Pass")
    else:
        print("Example 2: Fail")

