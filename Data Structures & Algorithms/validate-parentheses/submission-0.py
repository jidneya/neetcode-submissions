class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for c in s:
            print(stack)
            if (c in "([{"):
                stack.append(c)
            elif c in ")}]":
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()
            else:
                return False
        return len(stack) == 0
        