#!/usr/bin/env python
# Above line is needed to tell the script where python is located

def my_function():
  """ Do nothing, but document it.

  No, really, it doesnt do anything

  also adding a third line
  """
  pass

print my_function.__doc__

def fib2(n): # return fibonacci series up to n
  """ Return a list containing the fibonacci series up to n """

  result = []
  a, b = 0, 1
  while a < n :
    result.append(a)
    a, b = b, a + b
  return result

print fib2(100)

b = ("A", "B", "C", "D", "E", "F")
print(b[-2 : : -1])
