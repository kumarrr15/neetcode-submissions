class Solution:
    def isValid(self, s: str) -> bool:
        closed = {")": "(", "]": "[", "}":"{"}
        seen = []

        for char in s:
            if char in closed:
                if seen == [] or closed[char] != seen[-1]:
                    return False
                else:
                    seen.pop()
            else:
                seen.append(char)
        return seen == []