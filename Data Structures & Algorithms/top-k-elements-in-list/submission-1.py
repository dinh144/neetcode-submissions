class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(nums).most_common(k)
        res=[]
        for num, freq in temp:
            res.append(num)
        return res
        