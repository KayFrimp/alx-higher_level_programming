#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import fnmatch
    names = dir(hidden_4)
    pattern = "__*"
    for name in names:
        if fnmatch.fnmatch(name, pattern):
            continue
        print(name)
