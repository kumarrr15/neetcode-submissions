class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:       
        seen = set()
        longest = 0
        if nums == []:
            return 0

        for num in nums:
            if num not in seen:
                seen.add(num)
        
        for num in seen:
            if num - 1 not in seen:
                current = num
                length = 1
                while current + 1 in seen:
                    current += 1
                    length += 1
                longest = max(length, longest)
        return longest