class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        for letter in t:
            if letter not in letters or letters[letter] == 0:
                return False
            letters[letter] -= 1
        return True