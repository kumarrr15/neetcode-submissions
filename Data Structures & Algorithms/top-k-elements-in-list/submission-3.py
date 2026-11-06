from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for num in nums:            
            if num not in groups:
                groups[num] = 1
            else:
                groups[num] += 1
        sort = dict(sorted(groups.items(), key=itemgetter(1)))
        return list(sort.keys())[::-1][:k]