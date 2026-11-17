class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')':'(', "]": "[", "}":"{"}
        seen = []

        for char in s:
            if char in bracket:
                if seen == [] or seen[-1] != bracket[char]:
                    return False
                seen.pop()
            else:
                seen.append(char)
        return len(seen) == 0

