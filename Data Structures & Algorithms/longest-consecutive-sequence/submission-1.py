class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp= set(nums)

        res = 0
        for i in temp:
            if (i - 1) not in temp:
                count = 1
                while (i + count) in temp:
                    count += 1
                res = max(res, count)
        return res