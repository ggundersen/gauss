"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
----------------------------------------------------------------------------"""


def main():

    word = ''
    num_map = {
        '0' : ['',''],
        '1' : ['one', 'one'],
        '2' : ['two','twenty'],
        '3' : ['three', 'thirty'],
        '4' : ['four', 'forty'],
        '5' : ['five', 'fifty'],
        '6' : ['six', 'sixty'],
        '7' : ['seven', 'seventy'],
        '8' : ['eight', 'eighty'],
        '9' : ['nine', 'ninety'],
        '10' : ['ten'],
        '11' : ['eleven'],
        '12' : ['twelve'],
        '13' : ['thirteen'],
        '14' : ['fourteen'],
        '15' : ['fifteen'],
        '16' : ['sixteen'],
        '17' : ['seventeen'],
        '18' : ['eighteen'],
        '19' : ['nineteen'],
        'h' : ['hundredand']
    }
    
    for n in range(1,1000):
        if n < 20:
            word += num_map[str(n)][0]
        elif n < 100:
            word += num_map[str(n)[0]][1] + num_map[str(n)[1]][0]
        elif str(n)[1:] == '00':    # 100, 200, 300, &c.
            word += num_map[str(n)[:1]][0] + num_map['h'][0][:7]
        elif n < 1000 and int(str(n)[1:]) < 20 and int(str(n)[1:]) > 9:    # the teens
            word += num_map[str(n)[0]][0] + num_map['h'][0] + num_map[str(n)[1:]][0]
        elif n < 1000:
            word += num_map[str(n)[0]][0] + num_map['h'][0] + num_map[str(n)[1:2]][1] + num_map[str(n)[2:]][0]
    word += 'onethousand'
    return len(word)