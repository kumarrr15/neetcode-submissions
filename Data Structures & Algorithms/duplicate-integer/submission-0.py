class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct = []
        for i in range(0, len(nums)):
            if nums[i] in distinct:
                return True
            else:
                distinct.append(nums[i])
        return False