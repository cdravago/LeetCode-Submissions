class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "[":"]", "{":"}"}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[top] != c:
                    return False
        return not stack

            