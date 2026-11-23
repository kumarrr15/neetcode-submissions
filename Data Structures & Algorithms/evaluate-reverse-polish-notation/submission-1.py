class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        last2 = []
        for char in tokens:
            if char not in "+-*/":
                num = int(char)
                last2.append(num)
            else:
                if char == '+':
                    summ = last2[-1] + last2[-2]
                    last2.pop()
                    last2.pop()
                    last2.append(summ)
                elif char == '*':
                    prod = last2[-1] * last2[-2]
                    last2.pop()
                    last2.pop()
                    last2.append(prod)
                elif char == '-':
                    diff = last2[-2] - last2[-1]
                    last2.pop()
                    last2.pop()
                    last2.append(diff)
                else:
                    div = int(last2[-2] / last2[-1])
                    last2.pop()
                    last2.pop()
                    last2.append(div)
        return last2[0]