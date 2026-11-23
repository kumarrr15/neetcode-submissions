class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for char in tokens:
            if char not in "+-*/":
                num = int(char)
                nums.append(num)
            else:
                b = nums.pop()
                a = nums.pop()
                if char == '+':
                    nums.append(b + a)
                elif char == '*':
                    nums.append(b * a)
                elif char == '-':
                    nums.append(a - b)
                else:
                    nums.append(int(a / b))
        return nums[0]