#imports
import sys
import itertools
from pdb import set_trace
import numpy as np
import random
from mutators.tweak import Tweak
from mutators.change_special_character import ChangeSpecialCharacter
from mutators.add_padding import AddPadding
from mutators.tough_nut import ToughNut
from mutators.change_delimiter import ChangeDelimiter
from mutators.capitalize import Capitalize
from mutators.reduce import Reduce

# mutators
mutators = [ AddPadding, ToughNut, ChangeDelimiter, Capitalize, Reduce ]

# unpack command line args
assert len(sys.argv) == 4, "missing arguments"
n, input_filename, output_filename = sys.argv[1:]
n = int(n)
passwords = [ line.rstrip('\n') for line in open(input_filename) ]

# import rockyou
rockyou_passwords = [ line.strip().split(" ")[-1] for line in open("data/top_100_passwords.txt") ]

# create honeywords
output_file = open(output_filename, "w+")
for password in passwords:
    # choose random password seeds
    if n < 5:
        num_random_seed_passwords = n - 1
    else:
        num_random_seed_passwords = (n // 2) - 1
    seed_passwords = [ password ] + random.sample(rockyou_passwords, num_random_seed_passwords)
    np.random.shuffle(seed_passwords)
    seed_generator = itertools.cycle(seed_passwords)
    # generate honeywords
    honeywords = set([ password ])
    while len(honeywords) < n:
        seed = seed_generator.__next__()
        mutator = random.choice(mutators)
        while not mutator.matches(seed):
            mutator = random.choice(mutators)
        honeywords.add(mutator.run(seed))
    honeywords = list(honeywords)
    np.random.shuffle(honeywords)
    output_file.write(" ".join(honeywords) + "\n")
