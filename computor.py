#!/usr/bin/python2.7

import sys
import types
from expression import Expression
from treatment import resolveSecondDegree
from treatment import resolveFirstDegree
from treatment import resolveEquation

def findPolynom(reduceForm):
    polynomes = []
    for elem in reduceForm.subExpr:
        if elem.exponent % 1 != 0:
            print "\033[1;35mThe exponent is not an integer, I can't solve.\033[0m"
            exit()
        polynomes.append(elem.exponent)
    polynome = max(polynomes)
    if polynome > 2:
        print("\033[1;35mThe polynomial degree is stricly greater than 2, I can't solve.\033[0m")
        exit()
    else:
        print("\033[1;35mPolynomial degree: %d\033[0m" % polynome)
    return polynome;

def getEquations(equation):
    char = ['X', 'x', '=', '+', '-', '*', '^', ' ', '.']
    for c in equation:
        if c.isdigit() or c in char:
            pass
        else:
            print "\033[91mArgument Error.\033[0m"
            exit()
    try:
        [left, right] = equation.split('=')
    except:
        raise Exception("Error Equation")
    leftExpression = Expression(left)
    rightExpression = Expression(right)

    # Forme reduite
    #===============================
    reduceForm = rightExpression - leftExpression
    print "\033[1;33mreduce form : %s = 0\033[0m" % (reduceForm)

    # Polynome
    #===============================
    poly = findPolynom(reduceForm)
    if poly == 2:
        resolveSecondDegree(reduceForm.subExpr)
    elif poly == 1:
        resolveFirstDegree(reduceForm.subExpr)
    else:
        resolveEquation(reduceForm.subExpr)

def main():
    if len(sys.argv) == 2:
        try:
            getEquations(sys.argv[1])
        except Exception, e:
            print e
            sys.exit()
    else:
        print("\033[91mArgument Error.\033[0m")

if  __name__ =='__main__':
    main()
