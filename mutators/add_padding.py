from pdb import set_trace
import numpy as np
import random
from mutators.base_matcher import BaseMatcher

padding_characters = set(["!", "!!", "!!!", "*", "**", "***", "123", "123456"])

class AddPadding(BaseMatcher):
    @classmethod
    def run(self, password):
        return password + random.sample(padding_characters, 1)[0]
