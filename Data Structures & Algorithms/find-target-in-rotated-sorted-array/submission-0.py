class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            a = nums.index(target)
        else :
            return -1
        
        return a
        