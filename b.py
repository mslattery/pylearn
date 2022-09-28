import timeit

import numpy

def while_loop(n=100_000_000):
  i = 0
  s = 0
  while i < n:
    s += 1
    i += 1
  return s

def for_loop(n=100_000_000):
  s = 0
  for i in range(n):
    s += 1
  return s

def sum_range(n=100_000_000):
  return sum(range(n))

def sum_numpy(n=100_000_000):
  return numpy.sum(numpy.arange(n))

def sum_math(n=100_000_000):
  return (n * (n - 1)) // 2

def main():
  #print('while loop\t\t', timeit.timeit(while_loop, number=1))
  #print('for pure\t\t', timeit.timeit(for_loop, number=1))
  print('for pure\t\t', timeit.timeit(sum_range, number=1))
  print('for numpy\t\t', timeit.timeit(sum_numpy, number=1))
  print('for math\t\t', timeit.timeit(sum_math, number=1))

if __name__ == "__main__":
  main()