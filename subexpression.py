#!/usr/bin/python2.7

class SubExpression:

	def __init__(self, expression):
		if isinstance(expression, str):
			self.subexpr = expression
			self.coefficient = self.getCoefficient(expression)
			self.exponent = self.getExponent(expression)
			self.operand = self.getOperand()
			self.unknown = self.getUnknown()
		elif isinstance(expression, list):
			self.subexpr = expression
			self.coefficient = expression[0]
			self.exponent = expression[1]
			self.operand = self.getOperand()
			self.unknown = self.getUnknown()
		else:
			return "Error" ;

	def getCoefficient(self, expression):
		tab = expression.split('*')
		coeff = float(tab[0])
		return coeff ;

	def getExponent(self, expression):
		tab = expression.split('^')
		if len(tab) == 2 :
			expo = float(tab[1])
		else:
			expo = 0;
		return expo ;

	def getOperand(self):
		return '*' ;

	def getUnknown(self):
		return "X^" ;

	def __mul__(self, value):
		return SubExpression([self.coefficient * value, self.exponent])

	def __repr__(self):
		if self.exponent == 0:
			return "%.1f" % (self.coefficient) ;
		elif self.exponent % 1 == 0:
			return "%.1f * X^%.0f" % (self.coefficient, self.exponent)
		else:
			return "%.1f * X^%.1f" % (self.coefficient, self.exponent)

