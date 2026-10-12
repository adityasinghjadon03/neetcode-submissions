class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in d and stack:
                if d[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        