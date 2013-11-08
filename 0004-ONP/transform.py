#!/usr/bin/env python
"""
https://www.spoj.pl/problems/ONP/
Transform algebraic expression into RPN
"""

import sys


def torpn(expr):
    """torpn(['a', '+', 'b']) == ['a', 'b', '+']
    """
    operators = {'+': 0, '-': 0,
                 '*': 1, '/': 1,
                 '^': 2}
    op_stack = [[]]
    stack = [[]]

    while expr:
        char = expr.pop(0)

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

    return stack[-1]

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    for i in xrange(n):
        print ''.join(torpn(list(lines[i+1].strip())))

