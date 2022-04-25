# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phoneBtn = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if len(digits) is 0:
            return []
        res = []
        self.dfs(digits, 0, phoneBtn, '', res)
        return res
    
    # Depth-first search.
    def dfs(self, digits, index, phoneBtn, path, res):
        # Base case.
        if index >= len(digits):
            res.append(path)
            return
        btnStr = phoneBtn[digits[index]]
        for i in btnStr:
            self.dfs(digits, index+1, phoneBtn, path+i, res)