class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:          
            ident = "".join(sorted(word))
            if ident not in groups:
                groups[ident] = []
            groups[ident].append(word)
        return list(groups.values())
