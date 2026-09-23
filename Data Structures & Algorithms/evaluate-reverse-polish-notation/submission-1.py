class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            match i:
                case "+":
                    b = s.pop()
                    a = s.pop()
                    a = a + b
                    s.append(a)
                case "-":
                    b = s.pop()
                    a = s.pop()
                    a = a - b
                    s.append(a)
                case "*":
                    b = s.pop()
                    a = s.pop()
                    a = a * b
                    s.append(a)
                case "/":
                    b = s.pop()
                    a = s.pop()
                    a = int(a / b)
                    s.append(a)
                case _:
                    s.append(int(i))
        return s[-1]
