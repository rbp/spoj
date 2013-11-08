import sys
import psyco
psyco.full()

def main():
    lines = sys.stdin.readlines()
    lines.pop(0)
    spaces = []

    sys.stdout.write("\n".join(map((lambda line: spaces.append(line.index(' ')) or
                str(
                    int(line[spaces[-1]-1::-1]) +
                    int(line[-2:spaces[-1]:-1])
                    )[::-1].lstrip('0')),
               lines)))

main()

