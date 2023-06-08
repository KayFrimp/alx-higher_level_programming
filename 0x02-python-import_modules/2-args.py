#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if (args == 1):
        print("{} argument:".format(args))
    elif (args == 0):
        print("{} arguments.".format(args))
    else:
        print("{} arguments:".format(args))
    pos = 1
    while (pos <= args):
        print("{}: {}".format(pos, argv[pos]))
        pos = pos + 1
