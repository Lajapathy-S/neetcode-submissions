class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set (nums)
        res = 0
        for i in nums_set :
            length, curr = 0,i
           
            while (curr) in nums_set:
                length = length +1
                curr=curr+1
            res = max(res,length)
        return res
        