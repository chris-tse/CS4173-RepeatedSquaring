# Fast Modular Exponentiation using Repeated Squaring

Programming Assignment 2 for CS 4173
Christopher Tse

This script performs fast modular using the repeated squaring method on the command line parameters passed in. This script should output the same value as the built-in `pow(a, b, n)` function and can be used to check for correctness.

## Requirements
* Python 3.6+

## Usage

**Note**: Script can be invoked with `python3` instead of executing the file directly if shebang location does not correspond on local machine. 


Run the script with parameters `a`, `b`, and `n` as eight digit hexadecimal strings according to `a^b mod n` as follows:

```
$ ./main.py <a> <b> <n>
```

The `-v` flag can be used to view the debug output at each iteration:

```
$ ./main.py -v <a> <b> <n>
```

Example:
```
$ ./main.py 00000001 12345678 12345678
1

$ ./main.py 7fffffff 7eeeeeee 7ddddddd
74e6476c
```

