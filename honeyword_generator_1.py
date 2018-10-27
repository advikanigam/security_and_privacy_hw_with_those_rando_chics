#imports
import sys
from pdb import set_trace
import numpy as np
import random
from mutators.tweak import Tweak
from mutators.change_special_character import ChangeSpecialCharacter
from mutators.add_padding import AddPadding
from mutators.tough_nut import ToughNut
from mutators.change_deliminator import ChangeDeliminator

# mutators
mutators = [ Tweak, ChangeSpecialCharacter, AddPadding, ToughNut, ChangeDeliminator ]

# unpack command line args
assert len(sys.argv) == 4, "missing arguments"
n, input_filename, output_filename = sys.argv[1:]
n = int(n)
passwords = [ line.rstrip('\n') for line in open(input_filename) ]

# create honeywords
output_file = open(output_filename, "w+")
for password in passwords:
    honeywords = set([ password ])
    while len(honeywords) < n:
        mutator = random.choice(mutators)
        if mutator.matches(password):
            honeywords.add(mutator.run(password))
    honeywords = list(honeywords)
    np.random.shuffle(honeywords)
    output_file.write(" ".join(honeywords) + "\n")
