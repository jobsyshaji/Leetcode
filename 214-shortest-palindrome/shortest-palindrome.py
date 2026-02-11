class Solution:
    def shortestPalindrome(self, s: str) -> str:
        x = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(x[i:]):
                return x[:i] + s