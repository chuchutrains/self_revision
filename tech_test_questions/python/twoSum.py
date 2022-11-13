# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexDict = dict()
        for i in range(len(nums)):
            secondNum = target - nums[i]
            if secondNum in indexDict:
                return [indexDict[secondNum], i]
            else:
                # Store 'i' index.
                indexDict[nums[i]] = i

