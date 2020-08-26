"""Module to calculate the Levenshtein edit distance of two strings

Based on faster two array method.
Levenshtein distance is the minimum number of edits to change one string
to another by replacing, deleting or inserting characters.
For more information refer https://en.wikipedia.org/wiki/Levenshtein_distance
"""

# Levenshtein Distance
class Levenshtein():
    def __init__(self):
        self.setParams()
    
    def setParams(self, s='', t=''):
        """Sets the initialized class parameters to user arguments"""
        self.s = s
        self.t = t
        self.s_len = len(s)
        self.t_len = len(t)

    def distance(self, s, t, replace_cost=1):
        """Returns an integer, the minimum number of edits"""
        self.setParams(s, t)
        # add first elem for 'empty string' index
        old_diff = [x for x in range(self.t_len + 1)]
        new_diff = [0]*(self.t_len + 1)

        # wrt the DP table of Levenshtein edits
        # we are at (x,y) and want to go to (x+1,y+1)
        # the y component is in the x_th diff array
        for x in range(self.s_len):
            # to get from 's' to t='', it took x+1 deletions (x zero indexed)
            new_diff[0] = x + 1
            for y in range(self.t_len):
                delete_cost = old_diff[y+1] + 1
                insert_cost = new_diff[y] + 1
                substi_cost = old_diff[y] + (0 if s[x]==t[y] else replace_cost)
                new_diff[y+1] = min(delete_cost, insert_cost, substi_cost)
            old_diff = [x for x in new_diff]
        return old_diff[-1]
    
    def ratio(self, s, t, with_distance=False):
        """Returns a float, the similarity ratio between strings"""
        # replace is essentially delete then insert, 2 operations
        lev_dist = self.distance(s, t, replace_cost=2)
        if with_distance:
            return (1 - (lev_dist / (self.s_len + self.t_len)), lev_dist)
        return 1 - (lev_dist / (self.s_len + self.t_len))


if __name__ == "__main__":
    lev = Levenshtein()
    print("Enter two strings.")
    s = input(">>> ")
    t = input(">>> ")
    print(f"The strings are {lev.distance(s, t)} edits away.")
    print(f"Difference ratio is {lev.ratio(s, t)}")