import sys
import psyco
psyco.full()

def main():
    sys.stdin.readline()
    lines = sys.stdin.readlines()
    spaces = []

    sys.stdout.write("\n".join(map((lambda line: spaces.append(line.index(' ')) or
                str(
                    int(line[spaces[-1]-1::-1]) +
                    int(line[-2:spaces[-1]:-1])
                    )[::-1].lstrip('0')),
               lines)))

main()
