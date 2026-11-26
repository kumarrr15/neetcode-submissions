class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        maxx = 0
        
        for right in range(len(s)):
            char = s[right]

            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            maxx = max((right - left + 1), maxx)
        return maxx