def main():
    import sys
    for line in sys.stdin.readlines():
        if line[:2] == "42":
            break
        print line

main()
