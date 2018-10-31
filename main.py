#! /usr/local/bin/python3
'''
Computes the result of a^b mod n using repeated squaring
'''


import sys

# Flag for verbose output
verbose = False
args = sys.argv
args.pop(0)
if args[0] == '-v':
    verbose = True
    args.pop(0)

# Parameter error checking
if len(args) != 3:
    print('Error: invalid format\nExamples:\n\tpython3 main.py 00000001 12345678 12345678\n\tpython3 main.py -v 00000001 12345678 12345678', file=sys.stderr)
    sys.exit(1)
    
a = int(args[0], 16)
b = int(args[1], 16)
n = int(args[2], 16)

if verbose:
    print(f'Computing {a}^{b} mod {n}')

# Convert exponent to binary
bbin = bin(b)[2:]
res = 1

if verbose:
    print(f'Base:{a}, Exp:{b}')
    print(f'Binary exp: {bbin}')

# Main loop
for i in bbin:
    res = (res * res) % n
    if (i == '1'):
        res = (res * a) % n
        
    if verbose:
        print(f'Current result:{res}')

if verbose:
    print(f'Final result: {res}')
    print(f'Final result in hex: {hex(res)[2:]}')
else:
    print(hex(res)[2:])