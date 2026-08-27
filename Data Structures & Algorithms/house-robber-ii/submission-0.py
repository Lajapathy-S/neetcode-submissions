class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,houses):
        rob1 = 0
        rob2 = 0

        for i in houses:
            current = max(rob1+i,rob2)
            rob1 = rob2
            rob2 = current
        return rob2
        