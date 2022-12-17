# LinearEquation

## 1. Linear Equation Solving Using Inverse Matrix

`Linear equation`

```math
AX = B
```

`Find the value of X to solve the equation`

```math
X = inverse(A) . B
```


### Example

```math
3x + 8y = 5
```
```math
4x + 11y = 7
```

#### find the value of x using inverse matrix

```python
A = [[3, 8], 
    [4, 11]]

B = [5, 7]

X = ?
```

```math
X = inverse(A) . B
```


#### Why not linear Regression to solve this problem.

Linear regression require more dataset to solve the problem. it will fit the line based on the row. If there is limited example so linear regression will not work as expected.

## Reference:

   [Solving Systems with Inverses](https://math.libretexts.org/Bookshelves/Algebra/Map%3A_College_Algebra_(OpenStax)/07%3A_Systems_of_Equations_and_Inequalities/708%3A_Solving_Systems_with_Inverses)

