from pdb import set_trace
import numpy as np
import random
from mutators.base_mutator import BaseMutator
import re

class Capitalize(BaseMutator):
    delimiters = set(" _-*@")

    @classmethod
    def match(self, password):
        return password[0] in (self.ALPHA_LOWERS + self.ALPHA_UPPERS)

    @classmethod
    def run(self, password):
        if password[0] in self.ALPHA_LOWERS:
            return password[0].upper() + password[1:]
        else:
            return password[0].lower() + password[1:]
