class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sub_str = []
        for word in words:
            for word_2 in words[1:]:
                if word_2 != word:
                    if word in word_2:
                        sub_str.append(word)
                    if word_2 in word:
                        sub_str.append(word_2)
        return list(set(sub_str))
        