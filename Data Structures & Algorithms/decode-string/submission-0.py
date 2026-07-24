class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_multiplier = 0
        for ch in s:
            if ch.isdigit():
                current_multiplier = current_multiplier * 10 + int(ch)
            elif ch == "[":
                stack.append((current_string, current_multiplier))
                current_string = ""
                current_multiplier = 0
            elif ch == "]":
                previous_string, multiplier = stack.pop()
                current_string = previous_string + current_string * multiplier
            else:
                current_string += ch
        return current_string

        