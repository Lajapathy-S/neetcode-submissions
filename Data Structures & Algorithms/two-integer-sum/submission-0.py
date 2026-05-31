class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in res : 
                return [res[diff],i]
            res[j] = i


        