class Solution:
    def isValid(self, s: str) -> bool:
        l1 = list(s)
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in l1:
            if i in mapping:
                if not stack or stack.pop() != mapping[i]:
                    return False
            else:
                stack.append(i)
        return not stack