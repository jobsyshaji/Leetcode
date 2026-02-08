class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        sign = 1
        if s[i] == '-' or s[i] == '+':
            if s[i] == '-':
                sign = -1
            i += 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        limit = INT_MAX // 10
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if result > limit or (result == limit and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        return sign * result
