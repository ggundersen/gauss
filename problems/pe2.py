import gmath as g

def main():
  
  div = 100
  ans = 0
  gen = g.gen_fibonacci()
  fib = gen.next()

  while fib < 4000000:
    if fib % div == 0:
      ans += fib
    fib = gen.next()
  return ans