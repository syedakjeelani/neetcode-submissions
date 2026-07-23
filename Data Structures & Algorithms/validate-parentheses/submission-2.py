class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for x in s:
            if x in lookup:
                if stack and stack[-1] == lookup[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False

        