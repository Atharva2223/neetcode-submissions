class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        print(s)
        print(t)
        if s == t:
            return True
        else:
            return False
        