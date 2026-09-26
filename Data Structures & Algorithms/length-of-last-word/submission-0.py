class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        words += s.split()
        return len(words[-1])

