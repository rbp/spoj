#!/usr/bin/env python
"""
https://www.spoj.pl/problems/ONP/
Transform algebraic expression into RPN
"""

import sys


def torpn(expr):
    """torpn('a+b') == 'ab+'
    """
    operators = {'+': 0, '-': 0,
                 '*': 1, '/': 1,
                 '^': 2}
    op_stack = [[]]
    stack = [[]]
    for char in expr:
        if char == '(':
            stack.append([])
            op_stack.append([])
        elif char == ')':
            while op_stack[-1]:
                stack[-1].append(op_stack[-1].pop())
            op_stack.pop()
            top = stack.pop()
            stack[-1].extend(top)
        elif char in operators:
            if op_stack[-1] and operators[op_stack[-1][-1]] >= operators[char]:
                stack[-1].append(op_stack[-1].pop())
            op_stack[-1].append(char)
        else:
            stack[-1].append(char)
    while op_stack[-1]:
        stack[-1].append(op_stack[-1].pop())

    return "".join(stack[-1])

n = sys.stdin.readline()
lines = sys.stdin.readlines()
output = [torpn(line.rstrip()) for line in lines]
print '\n'.join(output)
