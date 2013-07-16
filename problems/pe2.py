import gmath as g

def main(divisor):
  
  div = int(divisor)
  ans = 0
  gen = g.gen_fibonacci()
  fib = gen.next()

  while fib < 4000000:
    if fib % div == 0:
      ans += fib
    fib = gen.next()
  return divisor