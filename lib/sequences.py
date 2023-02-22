#!/usr/bin/env python3

def print_fibonacci(length):
    output = []
    if length > 0:
        output.append(0)
    if length > 1:
        output.append(1)
    while len(output) < length:
        output.append(output[-1] + output[-2])
    print(output)
print_fibonacci(5)

