class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            char_set = set()
            left = 0
            max_len = 0
            
            for right in range(len(s)):
                # Nếu gặp ký tự trùng, co cửa sổ từ bên trái cho đến khi hết trùng
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1

                # Thêm ký tự mới vào cửa sổ
                char_set.add(s[right])
                
                # Cập nhật độ dài lớn nhất
                max_len = max(max_len, right - left + 1)
                
            return max_len