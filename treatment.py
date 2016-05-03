#!/usr/bin/python2.7

# Polynome 2 => Dicriminant
#==============================

#init a b c ===================
def getA(equation):
	a = 0
	for elem in equation:
		if elem.exponent == 2:
			a = elem.coefficient
	return a ;

def getB(equation):
	b = 0
	for elem in equation:
		if elem.exponent == 1:
			b = elem.coefficient
	return b ;

def getC(equation):
	c = 0
	for elem in equation:
		if elem.exponent == 0:
			c = elem.coefficient
	return c ;

# racine caree =================
def squareRoot(nb):
	x = nb
	y = 1.0
	e = 0.000001
	while x-y > e:
		x = (x+y)/2
		y = nb/x
	return x ;

# resolution ===================
def solveImaginaryResult(equation, delta):
	a = getA(equation)
	b = getB(equation)
	sq = squareRoot(-delta)

	xr = (-b) / (2 * a)
	xi = (sq) / (2 * a)

	print "Discriminant is strictly \033[1;32mnegative\033[0m."
	print "There is no real solution but there are imaginary solutions:"
	print "x1: \033[1;34m%f + %fi\033[0m" % (xr, xi)
	print "x2: \033[1;34m%f - %fi\033[0m" % (xr, xi)

def solveOneResult(equation):
	a = getA(equation)
	b = getB(equation)

	if a == 0:
		x1 = 0
	else:
		x1 = (-b)/(2*a)
	print "\033[1;32mDiscriminant is equal to 0.\033[0m"
	print "The solution is:\nx= \033[1;34m%f\033[0m" % x1

def solveTwoResult(equation, delta):
	a = getA(equation)
	b = getB(equation)
	sq = squareRoot(delta)

	x1 = (-b-sq)/(2*a)
	x2 = (-b+sq)/(2*a)
	print "Discriminant is strictly \033[1;32mpositive\033[0m, the \033[1;32mtwo\033[0m solutions are:"
	print "x1 = \033[1;34m%f\n\033[0mx2 = \033[1;34m%f\033[0m" % (x1, x2)

def getDiscriminant(equation):
	a = getA(equation)
	b = getB(equation)
	c = getC(equation)

	delta = b**2
	delta += -4*a*c
	return delta ;

def resolveSecondDegree(equation):
	discriminant = getDiscriminant(equation)
	if discriminant > 0:
		solveTwoResult(equation, discriminant)
	elif discriminant == 0:
		solveOneResult(equation)
	else:
		solveImaginaryResult(equation, discriminant)

# Polynome 1 => Resolution
#==============================
def resolveFirstDegree(equation):
	b = getB(equation)
	c = getC(equation)

	if b == 0:
		x = 0
	else:
		x = (-c)/b
	print "The solution is :"
	print "x = \033[1;34m%f\033[0m" % (x)

# Polynome 0 => Resolution
#==============================
def resolveEquation(equation):
	for elem in equation:
		if elem.coefficient == 0:
			print "All real numbers are solutions."
		else:
			print "\033[91mIncorrect equation.\033[0m"
