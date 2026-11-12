class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(st) - 1

        while left < right:
            if st[left] == st[right]:
                left += 1
                right -= 1
            else:
                return False
        return True