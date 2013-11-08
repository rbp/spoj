#!/usr/bin/env python

# Spoj changed to Python 2.7, and Psyco isn't supported anymore.
#import psyco
#psyco.full()

def main():
    import sys

    lines = sys.stdin.readlines()
    lines.pop(0)
    spaces = []

    nums = map((lambda line: spaces.append(line.index(' ')) or
                str(
                    int(line[spaces[-1]-1::-1]) +
                    int(line[-2:spaces[-1]:-1])
                    )[::-1].lstrip('0')),
               lines)

    sys.stdout.write("\n".join(nums))

main()
