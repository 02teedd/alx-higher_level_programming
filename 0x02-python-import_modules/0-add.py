#!/usr/bin/python3
a = 1
b = 2

def add(x, y):
    return x + y

def print_(x, y):
    print(f"{x} + {y} = {add(x, y)}")

if __name__ == "__main__":

    print_(a, b)
