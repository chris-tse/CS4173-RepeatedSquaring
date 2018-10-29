#! /usr/local/bin/python3

import sys

verbose = False

args = sys.argv
args.pop(0)
if args[0] == '-v':
    verbose = True
    args.pop(0)

a = int(args[0], 16)
b = int(args[1], 16)
n = int(args[2], 16)

if verbose:
    print(f'Computing {a}^{b} mod {n}')

exp = b
base = a
res = 1

if verbose:
    print(f'Base:{base}, Exp:{exp}, Result:{res}')
while exp > 0:
    if exp % 2 == 0:
        base = (base * base) % n
        exp = int(exp / 2)
    else:
        res = (res * base) % n
        exp -= 1
    if verbose:
        print(f'Base:{base}, Exp:{exp}, Result:{res}')

if verbose:
    print(f'Final result: {res}')
    print(f'Final result in hex: {hex(res)[2:]}')
else:
    print(hex(res)[2:])