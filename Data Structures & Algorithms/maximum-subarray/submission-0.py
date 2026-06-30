class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        n = len(nums)

        total = 0
        max_sum = float("-inf")

        for i in range(0,n):
            total+=nums[i]

            max_sum = max(max_sum,total)

            if total < 0:
                total = 0
        return max_sum
        