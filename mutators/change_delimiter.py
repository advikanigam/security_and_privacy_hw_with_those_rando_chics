from pdb import set_trace
import numpy as np
import random
from mutators.base_mutator import BaseMutator
import re

class ChangeDelimiter(BaseMutator):
    delimiters = set("_-*@")

    @classmethod
    def match(self, password):
        for delimiter in self.delimiters:
            if password.count(delimiter) >= 2:
                return True

    @classmethod
    def run(self, password):
        for delimiter in self.delimiters:
            if password.count(delimiter) >= 2:
                new_delimiter = random.sample(self.delimiters - set(delimiter), 1)[0]
                return password.replace(delimiter, new_delimiter)
