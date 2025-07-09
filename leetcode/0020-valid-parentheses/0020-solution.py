class Solution:
    def isValid(self, s: str) -> bool:
        # List of acceptable opening and closing parentheses.
        # Matching open-close parentheses are in corresponding positions of the strings.
        opening = "({["
        closing = ")}]"

        stack = []
        for x in s:
            # Push opening parentheses to the stack
            if x in opening:
                stack.append(x)

            # Try to match a closing parenthesis to the top item of the stack
            else:
                if len(stack) == 0:
                    return False

                y = stack.pop()

                # Do x and y match?
                if not (y in opening and closing[opening.index(y)] == x):
                    return False

        return len(stack) == 0
