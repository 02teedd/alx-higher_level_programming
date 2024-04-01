#!/usr/bin/python3
a = 1
b = 2
exec(compile(open("add_0.py").read(), "add_0.py", 'exec'))
print("{} + {} = {}".format(a, b, add(a, b)))
