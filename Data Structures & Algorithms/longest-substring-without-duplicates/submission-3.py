class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxx = 0
        left = 0

        for char in s:
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char) 
            maxx = max(maxx, len(seen))
        return maxx