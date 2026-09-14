class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        lowercase_s = s.lower()
        while left < right:
            left_char = lowercase_s[left]
            right_char = lowercase_s[right]
            if left_char.isalnum() == False:
                left = left + 1
                continue
            if right_char.isalnum() == False:
                right = right - 1
                continue
            
            if lowercase_s[left] != lowercase_s[right]:
                return False
            left = left+1
            right = right - 1
        return True
        