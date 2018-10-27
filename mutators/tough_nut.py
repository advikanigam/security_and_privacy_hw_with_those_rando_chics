from pdb import set_trace
import numpy as np
import random
from mutators.base_matcher import BaseMatcher


class ToughNut(BaseMatcher):
    @classmethod
    def chance(self):
        return 0.3

    @classmethod
    def run(self, password):
        n = random.choice([ 16, 20, 32, 64 ])
        characters = set().union(self.ALPHA_LOWERS, self.ALPHA_UPPERS, self.NUMBERS, self.SYMBOLS)
        result = [ random.sample(characters, 1)[0] for _ in range(n) ]
        return "".join(result)
