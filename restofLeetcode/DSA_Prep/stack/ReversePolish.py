"""
This is just reverse polish notation. Can be done in one o(n) pass
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1 and tokens[0].isdigit() == True:
            return int(tokens[0])
        if len(tokens) == 1 and tokens[0].isdigit() == False and len(tokens[0]) != 1:
            # negative
            return int(tokesn[0])

        stack = []

        for char in tokens:
            if char.isdigit() == True:
                stack.append(char)
            # handle the minus case
            elif char.isdigit() == False and len(char) != 1:
                tmp = int(char[0:])
                stack.append((tmp))
            elif char.isdigit() == False:
                # found outside char
                n2, n1 = int(stack[-1]), int(stack[-2])
                stack.pop()
                stack.pop()
                if char == '+':
                    n3 = n1 + n2
                    stack.append(n3)
                elif char == '*':
                    n3 = n1 * n2
                    stack.append(n3)
                elif char == '/':
                    n3 = n1 / n2
                    n3 = int(n3)
                    stack.append(n3)
                elif char == '-':
                    n3 = n1 - n2
                    stack.append(n3)

        return stack[0]


