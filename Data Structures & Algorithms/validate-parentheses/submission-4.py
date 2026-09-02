class Solution:
    def isValid(self, s: str) -> bool:
        # If the character is an opening character, push it onto the stack
        # If the characetr is a closing character, check the top of the stack and if it the same type of character but an opening one, pop it off the stack
        # Continue until there is a mismatch or the stack is empty
        # If the stack becomes empty after popping all the other characters off, it is a valid string

        # Can use a map to map the opening and closing braces to eachother
        # Use the closing one as the key since we are going to get the value associated with that

        stack = []
        parenMap = {')':'(', ']':'[', '}':'{'}

        for char in s:

            if char in parenMap.values():
                stack.append(char)
            elif char in parenMap and stack and stack[-1] == parenMap[char]:
                stack.pop()
            else:
                return False

        return not stack
