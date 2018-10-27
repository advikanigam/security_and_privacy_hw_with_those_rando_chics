from pdb import set_trace
import numpy as np
import random
from mutators.base_matcher import BaseMatcher
import re


class ChangeSpecialCharacter(BaseMatcher):
    @classmethod
    def match(self, password):
        matcher = ".*[\{}].*".format("\\".join(list(self.SYMBOLS)))
        return not not re.match(matcher, password)

    @classmethod
    def run(self, password):
        special_char_indicies = [ idx for idx in range(len(password)) if password[idx] in self.SYMBOLS ]
        special_char_idx = random.choice(special_char_indicies)
        new_character = random.sample(self.SYMBOLS - set(password[special_char_idx]), 1)[0]
        return password[:special_char_idx] + new_character + password[special_char_idx + 1:]
