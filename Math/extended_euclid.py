def extendedEuclid(a,b):
   x = a; y = b
   oldolds = 1
   olds = 0
   oldoldt = 0
   oldt = 1
   while y != 0:
      q, r = divmod(x,y)
      x, y = y, r
      s = oldolds - q * olds
      t = oldoldt - q * oldt
      oldolds = olds
      oldoldt = oldt
      olds = s
      oldt = t
   return x, oldolds, oldoldt
