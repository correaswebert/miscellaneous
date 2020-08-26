"""Quine McCluskey's Method to find Minimal SoP equation"""

import math

# !!!: When considering dontcare, try both X as 0 and 1 to check validity

class QuineMcCluskeySOP:
    def __init__(self, minterms, dontcare=None):
        self.minterms = minterms
        self.dontcare = dontcare

        self.numterms = len(minterms)   # currently not including don't cares
        self.nbits = math.ceil(math.log2(max(minterms)))

        self.powerof2 = [2**i for i in range(self.nbits)]
        self.steps = []

    def numBitsOn(self, num):
        num = bin(num)[2:]      # remove 0b from bin str
        return num.count('1')   # number of bits turned on

    def todash01(self, stepno):
        groups = self.steps[stepno]
        group_repr = [[] * len(groups)]
        for 

    """
    XORing two numbers(groups) if returns a power of 2, then it's valid
    eg. 0011 ^ 0111 = 0100 => valid
        0101 ^ 1110 = 1010 => invalid
    """
    def groupify(self):
        group = [[] for i in range(self.nbits+1)]
        for i in self.minterms:
            group[self.numBitsOn(i)].append(i)
        self.steps.append(group)
        return group

    def pairify(self):
        self.groupify()
        step1_groups = self.steps[0]
        groups = []
        for i in range(len(step1_groups) - 1):
            current_group = step1_groups[i]
            next_group = step1_groups[i+1]
            pairs = []
            for num in current_group:
                for numX in next_group:
                    if num ^ numX in self.powerof2:
                        pairs.append((num, numX))
            groups.append(pairs)
        self.steps.append(groups)
        return groups

if __name__ == "__main__":
    quine = QuineMcCluskeySOP((0,1,2,3,5,7,8,9,11,15))
    # quine.groupify
    print(quine.pairify())
