import newton_raphson as nr

#polynomial = nr.createPoly()

def signum(x):
	if x > 0:
		return 1
	elif x == 0:
		return 0
	else:
		return -1


def findRoot(poly):
	degree = len(poly) - 1
	roots = []
	l_pos = r_pos = 0
	
	p = lambda x: nr.valueOfPolyAt(poly, x)
	
	l_val = r_val = 0
	l_temp, r_temp = p(l_pos), p(r_pos)

	while len(roots) < degree:
	
		if l_val > l_temp:
			if signum(l_val) != signum(l_temp):
				roots.append( nr.newtonRaphson(poly, min(l_val, l_temp) - 0.0000005, 1000) )
				
			l_val = l_temp
			
		if r_val > r_temp:
			if signum(r_val) != signum(r_temp):
				roots.append( nr.newtonRaphson(poly, min(r_val, r_temp) + 0.0000005, 1000) )
				
			r_val = r_temp
		
		
	return roots
	
	
print( findRoot([12, -7, 1]) )
	