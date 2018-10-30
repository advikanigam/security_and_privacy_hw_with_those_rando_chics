import random

class BaseMutator:

    ALPHA_LOWERS = set([ chr(int) for int in range(97,123) ])
    ALPHA_UPPERS = set([ chr(int) for int in range(65,91) ])
    NUMBERS = set([ str(n) for n in range(10) ])
    SYMBOLS = set("`~!@#$%^&*()_+-=`[]}{;:,.<>|")

    @classmethod
    def matches(self, password):
        r = random.random()
        return r < self.chance() and self.match(password)

    @classmethod
    def match(self, password):
        return True

    @classmethod
    def chance(self):
        return 1
