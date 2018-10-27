from pdb import set_trace
import numpy as np
import random
from mutators.base_matcher import BaseMatcher
import re

class ChangeDeliminator(BaseMatcher):
    deliminators = set(" _-*@")

    @classmethod
    def match(self, password):
        for deliminator in self.deliminators:
            if password.count(deliminator) >= 2:
                return True

    @classmethod
    def run(self, password):
        for deliminator in self.deliminators:
            if password.count(deliminator) >= 2:
                new_deliminator = random.sample(self.deliminators - set(deliminator), 1)[0]
                return password.replace(deliminator, new_deliminator)
