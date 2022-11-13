# https://leetcode.com/problems/top-k-frequent-elements/solution/

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k is len(nums):
            return nums
        count = Counter(nums)
        # top nth, key, value.
        return heapq.nlargest(k, count.keys(), key=count.get)
