import gmath as g
import time

def pe2():
	return ''

def magic(divisor):
  fgen = g.gen_fibonacci()
  html = ''
  for i in range(1000):
    f = fgen.next()
    if f % int(divisor) == 0:
      f = bin(f)[2:]
      html += '<tr>'
      for d in f:
      	if d == '0':
      		html += '<td class="cell"></td>'
      	else:
      		html += '<td class="cell black"></td>'
      html += '</tr>'
  return html