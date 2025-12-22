class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        st = 0
        e = 0
        
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1
        
        for i in range(n):
            l1, r1 = expand(i,i)
            if r1-l1 > e-st:
                st, e = l1, r1
            
            l2, r2 = expand(i, i+1)
            if r2-l2 > e-st:
                st, e = l2, r2
        return s[st: e+1]