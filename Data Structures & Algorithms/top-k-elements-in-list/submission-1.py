class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        
        top_keys = sorted(res, key=res.get, reverse=True)[:k]
        return top_keys
          