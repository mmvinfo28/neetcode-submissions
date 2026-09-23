class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {"}":"{","]":"[",")":"("}
        for i in s:
            match i:
                case "{" | "(" | "[":
                    stack.append(i)
                case _:
                    j = maps[i]
                    if len(stack) == 0 or stack[-1] != j:
                        return False
                    stack.pop()
        return len(stack) == 0
        