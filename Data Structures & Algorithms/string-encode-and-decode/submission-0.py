class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            
            length_s = int(s[i:j])

            j += 1
            length_w = j + length_s
            w = s[j:length_w]

            res.append(w)
            i = length_w
        return res