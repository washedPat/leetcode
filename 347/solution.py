from typing import *
import heapq

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        # make frequency map of characters
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
       
        # push to heap
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            # we do this because we want to keep the heap size to k
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _, num in heap]