class Solution:

    def backtracker_sum(self,index,subset,total,nums,target,result):

        if index >= len(nums):
            return
        elif total == target:
            result.append(subset.copy())
            return
        if total > target:
            return



        subset.append(nums[index])
        sum = total+ nums[index]
        self.backtracker_sum(index,subset,sum,nums,target,result)
        subset.pop()
        sum = total
        self.backtracker_sum(index+1,subset,sum,nums,target,result)
    


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracker_sum(0,[],0,candidates, target,result)
        return result