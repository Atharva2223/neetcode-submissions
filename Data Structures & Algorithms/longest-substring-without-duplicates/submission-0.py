class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        my_dict = {}
        left, right = 0,0
        max_count = 0
        n = len(s)

        while right < n:

            if s[right] in my_dict:
                left = max((left, my_dict[s[right]]+1))


            max_count = max(max_count, right - left +1)
            my_dict[s[right]] = right
            right+=1
        return max_count
        


        