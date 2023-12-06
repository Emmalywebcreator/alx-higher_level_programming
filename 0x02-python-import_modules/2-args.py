#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    num_args = len(argv)
    print("{} argument{}".format(
        num_args, "s" if num_args != 1 else "",), end="")
    print(":" if num_args > 0 else ".")

    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
