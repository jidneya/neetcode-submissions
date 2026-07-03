class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed = [c.lower() for c in s if c.isalnum()]
        return removed[::-1] == removed