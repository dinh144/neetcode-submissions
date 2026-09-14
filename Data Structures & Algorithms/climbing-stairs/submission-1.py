class Solution:
    def climbStairs(self, n: int) -> int:
        # Sử dụng một dictionary làm bộ nhớ tạm (memo)
        memo = {}
        
        def helper(steps: int) -> int:
            # Bài toán cơ sở (Base cases)
            if steps == 1: return 1
            if steps == 2: return 2
            
            # Nếu đã tính toán bước này rồi, lấy luôn từ bộ nhớ ra
            if steps in memo:
                return memo[steps]
            
            # Công thức đệ quy: F(n) = F(n-1) + F(n-2)
            memo[steps] = helper(steps - 1) + helper(steps - 2)
            return memo[steps]
            
        return helper(n)
