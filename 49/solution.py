from collections import defaultdict
from typing import List
"""
49: Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    """
    naive idea:
        result_list = []
        for each word in the list
            find anagrams in list

    better idea:
        map = {}
        for each word in list:
            sort_word = sort(word)
            map[sort_word].append(word)

        return map values

    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            mp[sorted_word].append(word)

        return list(mp.values())
