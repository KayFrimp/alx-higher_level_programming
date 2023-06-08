#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    pos = 1
    result = 0
    while (pos <= args):
        result = result + int(argv[pos])
        pos = pos + 1
    print("{}".format(result))
