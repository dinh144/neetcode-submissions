class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = [c.lower() for c in s if c.isalnum()]
        return temp == temp[::-1]