class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for char in tokens:
            if char not in "+-*/":
                num = int(char)
                nums.append(num)
            else:
                if char == '+':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(b + a)
                elif char == '*':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(b * a)
                elif char == '-':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(a - b)
                else:
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(int(a / b))
        return nums[0]