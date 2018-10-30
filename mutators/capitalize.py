from pdb import set_trace
import numpy as np
import random
from mutators.base_mutator import BaseMutator
import re

class Capitalize(BaseMutator):
    delimiters = set(" _-*@")

    @classmethod
    def match(self, password):
        return password[0] in self.ALPHA_LOWERS

    @classmethod
    def run(self, password):
        return password[0].upper() + password[1:]
