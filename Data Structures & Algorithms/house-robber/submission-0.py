class Solution:
    def solve(self, index, nums,dp):
        if index == 0:
            return nums[index]
        if index == -1:
            return 0
        if dp[index]!=-1:
            return dp[index]
        pick = nums[index] + self.solve(index - 2, nums,dp)
        notpick = 0 + self.solve(index - 1, nums,dp)
        dp[index] = max(pick, notpick)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] *(n+1)
        n = len(nums)
        return self.solve(n - 1, nums,dp)