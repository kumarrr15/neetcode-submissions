class Solution:
    def validPalindrome(self, s: str) -> bool:
        res=""
        for c in s:
            if c.isalnum():
                res += c.lower()
        
        for i in range(len(res)):
            st = res[:i] + res[i+1:]
            if st[::-1] == st:
                return True
        return False