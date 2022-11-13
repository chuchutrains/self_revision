# https://leetcode.com/problems/4sum/submissions/

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def kSum(nums, target, k):
            print("t=",target,"k=",k)
            res = []
            
            # If we have run out of numbers to add, return res.
            if not nums:
                return res
            
            # There are k remaining values to add to the sum. The 
            # average of these values is at least target // k.
            average_value = target // k
            
            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest 
            # value in nums is smaller than target // k.
            # Eg. nums = [5,7,9,11,13], target is 8 and k is 4. average_value
            # will be 8/4=2, it will be impossible to sum 4 value to reach
            # target of 8 because 5+7+9+11=32 OR we need an average value of 2
            # or lower.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
            # Recursive base case.
            if k == 2:
                return twoSum(nums, target)
                
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    # Recursive move toward the base case.
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        # i+1 = i + kSum(i-1)
                        res.append([nums[i]] + subset)
    
            return res

        def twoSum(nums, target):
            res = []
            lo, hi = 0, len(nums) - 1
    
            while (lo < hi):
                curr_sum = nums[lo] + nums[hi]
                # Prevent duplicate.
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                # Prevent duplicate.
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                                                         
            return res

        nums.sort()
        return kSum(nums, target, 4)