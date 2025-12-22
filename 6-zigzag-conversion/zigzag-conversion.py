class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= 1:
            return s

        idx = 0
        d = 1
        res = [""] * numRows
        for ch in s:
            res[idx] += ch
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        
        return "".join(res)