class Solution:
    def solve(self, index,subset,ch_map, digits, result):
        if len(digits) == 0:
            return []
        if index >= len(digits):
            result.append("".join(subset))
            return 
        for ch in ch_map[digits[index]]:
            subset.append(ch)
            self.solve(index+1,subset,ch_map,digits, result)
            subset.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        ch_map ={
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        self.solve(0,[],ch_map,digits, result)
        return result
