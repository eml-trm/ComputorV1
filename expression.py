#!/usr/bin/python2.7

from subexpression import SubExpression

class Expression:

	def __init__(self, expression):
		if isinstance(expression, str):
			self.expression = self.getExpression(expression)
			self.subExpr = self.getSubexpr()
		elif isinstance(expression, list):
			self.subExpr = expression
		self.gatherExpression(self)

	def gatherExpression(self, bigExpression):
		smallExpression = []
		exposant = self.getExposant(bigExpression)
		for eachExpo in exposant:
			if self.getCoefficient(eachExpo, bigExpression) != 0:
				smallExpression.append(SubExpression([self.getCoefficient(eachExpo, bigExpression), eachExpo]))
		if smallExpression == []:
			smallExpression.append(SubExpression([0, 0]))
		self.subExpr = smallExpression;

	def getExpression(self, expression):
		newExpr = expression.replace(" + ", " & ")
		newExpr = newExpr.replace(" +", "")
		newExpr = newExpr.replace("- ", "+ -")
		newExpr = newExpr.replace("&", "+")
		newExpr = newExpr.replace(" ", "")
		return newExpr;

	def getSubexpr(self):
		tab = []
		for subExpress in self.expression.split("+"):
			tab.append(SubExpression(subExpress))
		return tab;

	def getCoefficient(self, nb, expression):
		newList = []
		coeff = 0
		for x, element in enumerate(expression.subExpr):
			if expression.subExpr[x].exponent == nb:
				coeff += expression.subExpr[x].coefficient
		newList = coeff
		return newList;

	def getExposant(self, expression):
		tab = []
		for x, elem in enumerate(expression.subExpr):
			if expression.subExpr[x].exponent in tab:
				continue ;
			else:
				tab.append(expression.subExpr[x].exponent)
		return tab

	def __sub__(self, rhs):
		newList = []
		exponentList = []
		expo = self.getExposant(self)
		expo += rhs.getExposant(rhs)
		for nb in expo:
			if nb not in exponentList:
				exponentList.append(nb)
		for nb in exponentList:
			if nb == None:
				pass
			else:
				newList.append(SubExpression([self.getCoefficient(nb, self) + (rhs.getCoefficient(nb, rhs) * -1), nb]))
		return Expression(newList) ;

	def __mul__(self, value):
		return Expression([i * value for i in self.subExpr]);

	def __repr__(self):
		return "Expression: %s" % (self.expression)

	def __str__(self):
		return " + ".join([str(i) for i in self.subExpr])
