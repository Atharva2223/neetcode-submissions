class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      HMap = {}

      for i,n in enumerate(nums):
        diff = target - n
        if diff in HMap:
            return [HMap[diff],i]
        HMap[n] = i



        
                
         