class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = [1] * len(nums)
        prefix = 1
        res = []

        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


            