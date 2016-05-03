# ComputorV1
#### First project in Python

This program solves a polynomial equation of degree less than or equal to 2.

## Summary
 1. [Usage](#usage)
 2. [Example](#example)


## <a name="usage">Usage</a>

```
./computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
```

## <a name="example">Example</a>

###### Equation degree 2
```
./computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

reduce form : -4.0 + -4.0 * X^1 + 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
x1 = -0.475131
x2 = 0.905239
```
###### Equation degree 1
```
./computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"

reduce form : -1.0 + -4.0 * X^1 = 0
Polynomial degree: 1
The solution is :
x = -0.250000
```

###### Equation degree 3
```
./computor.py  "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"

3 = 3 * X^0"
reduce form : -5.0 + 6.0 * X^1 + 5.6 * X^3 = 0
The polynomial degree is stricly greater than 2, I can't solve.
```


###### Particular case
```
./computor.py "42 * X^0 = 42 * X^0"

reduce form : 0.0 = 0
Polynomial degree: 0
All real numbers are solutions.
```





