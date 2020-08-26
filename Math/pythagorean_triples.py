# Rosetta Code - Pythagorean Triples

from fractions import gcd
 
# Naive method  
def pt1(maxperimeter=100):
    
    trips = []
    for a in range(1, maxperimeter):
        aa = a*a
        for b in range(a, maxperimeter-a+1):
            bb = b*b
            for c in range(b, maxperimeter-b-a+1):
                cc = c*c
                if a+b+c > maxperimeter or cc > aa + bb: break
                if aa + bb == cc:
                    trips.append((a,b,c, gcd(a, b) == 1))
    return trips
 
def pytrip(trip=(3,4,5),perim=100, prim=1):
    a0, b0, c0 = a, b, c = sorted(trip)
    t, firstprim = set(), prim>0
    while a + b + c <= perim:
        t.add((a, b, c, firstprim>0))
        a, b, c, firstprim = a+a0, b+b0, c+c0, False
    #
    t2 = set()
    for a, b, c, firstprim in t:
        a2, a5, b2, b5, c2, c3, c7 = a*2, a*5, b*2, b*5, c*2, c*3, c*7
        if  a5 - b5 + c7 <= perim:
            t2 |= pytrip(( a - b2 + c2,  a2 - b + c2,  a2 - b2 + c3), perim, firstprim)
        if  a5 + b5 + c7 <= perim:
            t2 |= pytrip(( a + b2 + c2,  a2 + b + c2,  a2 + b2 + c3), perim, firstprim)
        if -a5 + b5 + c7 <= perim:
            t2 |= pytrip((-a + b2 + c2, -a2 + b + c2, -a2 + b2 + c3), perim, firstprim)
    return t | t2


# Parent/child relationship method:
# http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#XI. 
def pt2(maxperimeter=100):

    trips = pytrip((3,4,5), maxperimeter, 1)
    return trips
 
def printit(maxperimeter=100, pt=pt1):
    trips = pt(maxperimeter)
    print("  Up to a perimeter of %i there are %i triples, of which %i are primitive"
          % (maxperimeter,
             len(trips),
             len([prim for a,b,c,prim in trips if prim])))
 
for algo, mn, mx in ((pt1, 250, 2500), (pt2, 500, 20000)):
    print(algo.__doc__)
    for maxperimeter in range(mn, mx+1, mn):
        printit(maxperimeter, algo)
 

'''

Output

# Naive method
    
  Up to a perimeter of 250 there are 56 triples, of which 18 are primitive
  Up to a perimeter of 500 there are 137 triples, of which 35 are primitive
  Up to a perimeter of 750 there are 227 triples, of which 52 are primitive
  Up to a perimeter of 1000 there are 325 triples, of which 70 are primitive
  Up to a perimeter of 1250 there are 425 triples, of which 88 are primitive
  Up to a perimeter of 1500 there are 527 triples, of which 104 are primitive
  Up to a perimeter of 1750 there are 637 triples, of which 123 are primitive
  Up to a perimeter of 2000 there are 744 triples, of which 140 are primitive
  Up to a perimeter of 2250 there are 858 triples, of which 156 are primitive
  Up to a perimeter of 2500 there are 969 triples, of which 175 are primitive

# Parent/child relationship method:
# http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#XI.
    
  Up to a perimeter of 500 there are 137 triples, of which 35 are primitive
  Up to a perimeter of 1000 there are 325 triples, of which 70 are primitive
  Up to a perimeter of 1500 there are 527 triples, of which 104 are primitive
  Up to a perimeter of 2000 there are 744 triples, of which 140 are primitive
  Up to a perimeter of 2500 there are 969 triples, of which 175 are primitive
  Up to a perimeter of 3000 there are 1204 triples, of which 211 are primitive
  Up to a perimeter of 3500 there are 1443 triples, of which 245 are primitive
  Up to a perimeter of 4000 there are 1687 triples, of which 280 are primitive
  Up to a perimeter of 4500 there are 1931 triples, of which 314 are primitive
  Up to a perimeter of 5000 there are 2184 triples, of which 349 are primitive
  Up to a perimeter of 5500 there are 2442 triples, of which 385 are primitive
  Up to a perimeter of 6000 there are 2701 triples, of which 422 are primitive
  Up to a perimeter of 6500 there are 2963 triples, of which 457 are primitive
  Up to a perimeter of 7000 there are 3224 triples, of which 492 are primitive
  Up to a perimeter of 7500 there are 3491 triples, of which 527 are primitive
  Up to a perimeter of 8000 there are 3763 triples, of which 560 are primitive
  Up to a perimeter of 8500 there are 4029 triples, of which 597 are primitive
  Up to a perimeter of 9000 there are 4304 triples, of which 631 are primitive
  Up to a perimeter of 9500 there are 4577 triples, of which 667 are primitive
  Up to a perimeter of 10000 there are 4858 triples, of which 703 are primitive
  Up to a perimeter of 10500 there are 5138 triples, of which 736 are primitive
  Up to a perimeter of 11000 there are 5414 triples, of which 770 are primitive
  Up to a perimeter of 11500 there are 5699 triples, of which 804 are primitive
  Up to a perimeter of 12000 there are 5980 triples, of which 839 are primitive
  Up to a perimeter of 12500 there are 6263 triples, of which 877 are primitive
  Up to a perimeter of 13000 there are 6559 triples, of which 913 are primitive
  Up to a perimeter of 13500 there are 6843 triples, of which 949 are primitive
  Up to a perimeter of 14000 there are 7129 triples, of which 983 are primitive
  Up to a perimeter of 14500 there are 7420 triples, of which 1019 are primitive
  Up to a perimeter of 15000 there are 7714 triples, of which 1055 are primitive
  Up to a perimeter of 15500 there are 8004 triples, of which 1089 are primitive
  Up to a perimeter of 16000 there are 8304 triples, of which 1127 are primitive
  Up to a perimeter of 16500 there are 8595 triples, of which 1159 are primitive
  Up to a perimeter of 17000 there are 8884 triples, of which 1192 are primitive
  Up to a perimeter of 17500 there are 9189 triples, of which 1228 are primitive
  Up to a perimeter of 18000 there are 9484 triples, of which 1264 are primitive
  Up to a perimeter of 18500 there are 9791 triples, of which 1301 are primitive
  Up to a perimeter of 19000 there are 10088 triples, of which 1336 are primitive
  Up to a perimeter of 19500 there are 10388 triples, of which 1373 are primitive
  Up to a perimeter of 20000 there are 10689 triples, of which 1408 are primitive

'''

# Barebone minimum for this task:
from sys import setrecursionlimit
setrecursionlimit(2000) # 2000 ought to be big enough for everybody
 
def triples(lim, a = 3, b = 4, c = 5):
    l = a + b + c
    if l > lim: return (0, 0)
    return reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), [
        (1, lim / l),
        triples(lim,  a - 2*b + 2*c,  2*a - b + 2*c,  2*a - 2*b + 3*c),
        triples(lim,  a + 2*b + 2*c,  2*a + b + 2*c,  2*a + 2*b + 3*c),
        triples(lim, -a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c) ])
 
for peri in [10 ** e for e in range(1, 8)]:
    print peri, triples(peri)

'''

Output:

10 (0, 0)
100 (7, 17)
1000 (70, 325)
10000 (703, 4858)
100000 (7026, 64741)
1000000 (70229, 808950)
10000000 (702309, 9706567)

'''
