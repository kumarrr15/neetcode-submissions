class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            n = len(nums)
            if n != len(ans):
                ans.append(num)
            if n == len(ans):
                ans += nums
        return ans
