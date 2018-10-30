from pdb import set_trace
import numpy as np
import random
from mutators.base_mutator import BaseMutator

class Tweak(BaseMutator):
    @classmethod
    def chance(self):
        return 0.2

    @classmethod
    def _tweak_character(self, char):
        """
        returns new, random character of same type
        """
        if char in self.ALPHA_LOWERS:
            return random.sample(self.ALPHA_LOWERS - set(char), 1)[0]
        elif char in self.ALPHA_UPPERS:
            return random.sample(self.ALPHA_UPPERS - set(char), 1)[0]
        elif char in self.NUMBERS:
            return random.sample(self.NUMBERS - set(char), 1)[0]
        else:
            return random.sample(self.SYMBOLS - set(char), 1)[0]

    @classmethod
    def run(self, password):
        n = random.randint(1,3)
        indicies_to_tweak = random.sample(range(len(password)), n)
        result = list(password)
        for idx in indicies_to_tweak:
            result[idx] = self._tweak_character(result[idx])
        return "".join(result)
