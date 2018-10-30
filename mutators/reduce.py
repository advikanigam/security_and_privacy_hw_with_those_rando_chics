"""
removes trailing digits, or special characters
"""

from pdb import set_trace
import numpy as np
import random
from mutators.base_mutator import BaseMutator
import re

class Reduce(BaseMutator):
    delimiters = set(" _-*@")

    @classmethod
    def match(self, password):
        return not not re.match("^\w+[^a-zA-Z]+$", password)

    @classmethod
    def run(self, password):
        suffix_index = re.search("[^a-zA-Z]+$", password).span()[0]
        return password[0:suffix_index]
