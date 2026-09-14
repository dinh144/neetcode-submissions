class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Initialize the first two numbers of the relevant sequence
        # For n=3: we need the 4th Fibonacci number, which is 3
        prev2 = 1  # F(2)
        prev1 = 2  # F(3)
        
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1
