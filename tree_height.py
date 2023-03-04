# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    lib = {}
    for i in range(n):
        if i not in lib:
            max_height = 1
            bar = i
            while parents[bar] != -1:
                main = parents[bar]
                if main not in lib:
                    bar = main
                    max_height = max_height + 1
                else:
                    max_height = max_height + lib[main]
                    break
            lib[i] = max_height
    return max(lib.values())


def main():
    ievade = input()
    if "F" in ievade:
        fails = input()
        fails = "BR/" + fails
        if 'a' not in fails:
            try:
                with open(fails, "r") as f:
                    n = int(f.readline())
                    parents = numpy.array(list(map(int, f.readline().split())))
                    print (compute_height(n, parents))

            except FileNotFoundError:
                return print("File_not_found_error")
    if 'I' in ievade:
        n = int(input())
        parents = numpy.array(list(map(int, input().split())))
        print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
