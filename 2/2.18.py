# Tokenizing Text
# 2.18.1

text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'), ('NUM' , 42), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)' 
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# 2.18.2
scanner = master_pat.scanner('foo = 42')
scanner.match()
_.lastgroup, _.group()
scanner.match()
_.lastgroup, _.group()
scanner.match()
_.lastgroup, _.group()
scanner.match()
_.lastgroup(), _.group()
scanner.match()

# 2.18.3
from collections import namedtuple

Token = namedtuple('Token', ['type','value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group()) 

# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# 2.18.4
tokens = (tok for tok in generate_tokens(master_pat, text))
if tok.type != 'WS')
for tok in tokens:
    print(tok)


# Discussion
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))   # Correct

PRINT = r'(P<PRINT>print)'
NAME = r'(P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)

