class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        l, r = 0,0
        res = 0

        while r < len(s):
            while s[r] in seen:
                seen.pop(0)
                res = max(res, r-l)
                l +=1
            seen.append(s[r])
            r+=1
        res = max(res, r-l)
        return res
        