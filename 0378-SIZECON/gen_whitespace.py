#!/usr/bin/env python

# Generate whitespace string
# Attention: this prints to STDOUT, therefore includes an extra \n at the end

prog = "print len(''.join(' '*input() for j in range(input())))"

# Each char is length is space string (tab-separated)
# program = ''.join(chr(c) for c in [len(i) for i in p.split('	')])
#open('foo', 'w').write('	'.join(' '*ord(c) for c in prog))


# Each char is index of tab % (largest ord + 1).
max_ord = max([ord(c) for c in prog])
base = max_ord + 1
ords = []
s = ''
for c in prog:
    o = ord(c)
    m = o % base
    # pad to next multiple of base, if necessary
    if ords and o <= ords[-1]:
        s += ' '*(base - len(s)%base)
    s += ' '*(m - (len(s)%base)) + '	'
    ords.append(o)
    #print c, o, len(s), s.rfind('	')
print s
