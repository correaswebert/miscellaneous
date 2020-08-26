"""Module to calculate the Levenshtein edit distance of two strings

Based on dynamic programming.
Levenshtein distance is the minimum number of edits to change one string
to another by replacing, deleting or inserting characters.
For more information refer https://en.wikipedia.org/wiki/Levenshtein_distance
"""

# Levenshtein Distance
class Levenshtein():
    def __init__(self):
        self.str1 = ''
        self.str2 = ''
        self.strlen1 = 0
        self.strlen2 = 0
        self.diff_mat = [[0]]

    def setParams(self, str1, str2):
        """Sets the initialized class parameters to user arguments"""
        self.str1 = str1
        self.str2 = str2
        self.strlen1 = len(str1)
        self.strlen2 = len(str2)

        # add an extra row,col for 'empty string' index
        # rest rows,cols are for chars of str1 and str2
        self.diff_mat = [[0]*(self.strlen2 + 1) for _ in range(self.strlen1 + 1)]
        # set: empty string to str1 edit distance
        for x in range(self.strlen1 + 1):
            self.diff_mat[x][0] = x
        # set: empty string to str2 edit distance
        for y in range(self.strlen2 + 1):
            self.diff_mat[0][y] = y

    def distance(self, str1, str2, replace_cost=1):
        """Returns an integer, the minimum number of edits"""
        self.setParams(str1, str2)

        # Indexed from 1 to match the actual formula ... lil confusing for direct read
        for x in range(1, self.strlen1 + 1):
            for y in range(1, self.strlen2 + 1):
                cost = 0 if self.str1[x-1] == self.str2[y-1] else replace_cost
                # replace(no change if 0 cost), delete, insert operations resp.
                self.diff_mat[x][y] = min(
                                        self.diff_mat[x-1][y-1] + cost,
                                        self.diff_mat[x-1][y] + 1,
                                        self.diff_mat[x][y-1] + 1
                                    )
        return self.diff_mat[self.strlen1][self.strlen2]
    
    def ratio(self, str1, str2, with_distance=False):
        """Returns a float, the similarity ratio between strings"""
        # replace is essentially delete then insert, 2 operations
        lev_dist = self.distance(str1, str2, replace_cost=2)
        if with_distance:
            return (1 - (lev_dist / (self.strlen1 + self.strlen2)), lev_dist)
        return 1 - (lev_dist / (self.strlen1 + self.strlen2))


if __name__ == "__main__":
    lev = Levenshtein()
    print("Enter two strings.")
    str1 = input(">>> ")
    str2 = input(">>> ")
    print(f"The strings are {lev.distance(str1, str2)} edits away.")
    print(f"Difference ratio is {lev.ratio(str1, str2)}")
    # names = {
    #     "Pooja":    0,
    #     "Elisha":   0,
    #     "Lakshita": 0,
    #     "Rujuta":   0,
    #     "Shivangi": 0,
    #     "Sonal":    0,
    #     "Tanishta": 0,
    #     "Mayuri":   0,
    #     "Kalyani":  0,
    #     "Rhea":     0,
    #     "Swizel":   0,
    # }
    # for name in names:
    #     names[name] = round(lev.ratio('Swebert', name), 3) * 100
    
    # names = sorted(names.items(), key=lambda kv: (kv[1],kv[0]))
    # for name_val in names:
    #     name, similarity = name_val
    #     print(
    #         name.rjust(10, ' '),
    #         f"{similarity:2.3f}".rjust(6) + "% similarity"
    #     )
    
    # print("Swebert Correa was born on 11 January 2000.")