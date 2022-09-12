---
id: UZeo2oZpVHB988NvkP3eRa
title: Using Matrices to Translate, Rotate, and Reflect
version: 2022-09-11T16:57:45
tags: linear-algebra, matrices
---

--------------------------------------------------------------------------------------------

## Using Matrices to Translate, Rotate, and Reflect

One situation where matrices are useful is computing where points in a plane move to under
simple transformations - rotations, reflections, translations, and combinations of these.
We can think of matrices as a way to _organize_ the calculations needed to move points
arou

### A Quick Introduction to Matrices

A _matrix_ is a set of number organized as a rectangular block. For example:

$$
M = \left[\begin{array}{cc}
      1 & 2 \\
      3 & 4 \\
      5 & 6 \\
    \end{array}\right]
$$

is a $3 \times 2$ (read as "3 by 2" matrix). The first number is the number of horizontal
rows and the second number is the number of vertical columns.

We use subscripts to indicate the row and column of a particular element in the matrix. For
example, $M_{2, 1} = 3$ in the matrix $M$ above.

#### Adding Matrices

Two matrices can be added … but only if they are compatible by having the same number of
rows and columns. The sum of two matrices $A$ and $B$ is a matrix of the same size where
each element is the sum of the corresponding elements in $A$ and $B$.

##### Example

Suppose we have two matrices

$$
A = \left[\begin{array}{cc}
      1 & 2 \\
      3 & 4 \\
      5 & 6 \\
    \end{array}\right]
$$

and

$$
B = \left[\begin{array}{cc}
      7  & 8 \\
      9  & 10 \\
      11 & 12 \\
    \end{array}\right].
$$

These two matrices are compatible for calculating $A + B$ because they have the same number
of rows and columns. The sum of $A$ and $B$ is

$$
A + B = \left[\begin{array}{cc}
          8  & 10 \\
          12 & 14 \\
          16 & 18
        \end{array}\right].
$$

##### Exercises

1. Verify that the sum of $A$ and $B$ is the matrix above.

#### Multiplying Matrices

Two matrices $A$ and $B$ can be multiplied … but only if they are compatible by having the
number of columns of $A$ equal to the number of rows of $B$. To calculate element in the
$i$-th row and $j$-th column of the product of two matrices
$A$ and $B$, we use the following procedure:

* take $i$-th row of $A$ and the $j$-th column of $B$,

* pair up the elements of these two lists of numbers,

* multiply the pairs of elements to generate a new list of numbers, and

* add up all of the products of pairs of elements.

Organizing the results repeating this procedure for all of the possible combinations of
rows of $A$ and columns of $B$ into a new block gives us the product of $A$ and $B$.

##### Example

Suppose we have two matrices

$$
A = \left[\begin{array}{cc}
      1 & 2 \\
      3 & 4 \\
      5 & 6 \\
    \end{array}\right]
$$

and

$$
B = \left[\begin{array}{cc}
      7 & 8 \\
      9 & 10 \\
    \end{array}\right].
$$

These two matrices are compatible for calculating $A \times B$ because the number of
columns of $A$ and the number of rows of $B$ are the same (both equal to 2). If we call
the product $C$, we can use the procedure described above to calculate $C_{1,2}$.

* The first row of $A$ is $[1, 2]$ and the second columns of $B$ is $[8, 10]$.

* Using these two lists of numbers, we get the following list of pairs:

  $$
  [(1, 8), (2, 10)].
  $$

* Multiplying the pairs of elements, we get the new list:

  $$
  [8, 20].
  $$

* Finally, adding up the numbers in the last list, we find that $C_{1,2} = 28$.

Using this procedure for all combinations of rows of $A$ and columns of $B$, we can
calculate the product $A \times B$:

$$
A \times B = \left[\begin{array}{cc}
               25 & 28 \\
               57 & 64 \\
               89 & 100 \\
            \end{array}\right].
$$

##### Exercises

2. Verify that the product of $A$ and $B$ is the matrix above.

3. Are matrices $A$ and $B$ compatible if we want to compute the product $BA$?

#### Using Matrices to Represent Points in the Plane

A useful way to represent a _point_ in the plane is as a $2 \times 1$ matrix. For example,
the point $p = (2, 1)$ in the $xy$-plane can be represented as

$$
p = \left[\begin{array}{cc}
      2 \\
      1 \\
    \end{array}\right].
$$

### Using Matrices to Move Points Around the Plane

#### Translations

To calculate the position of any point $p = (x, y)$ in the plane after translating by an
amount $\Delta x$ in the $x$-direction and an mount $\Delta y$ in the $y$-direction, add
matrix representation of the point $p$ to a $2 \times 1$ matrix $T$ for the translation:

$$
T = \left[\begin{array}{c}
      \Delta x \\
      \Delta y \\
    \end{array}\right]
$$

The location of the point $p$ after translating $(\Delta x, \Delta y)$ is

$$
\left[\begin{array}{c}
  x + \Delta x \\
  y + \Delta y \\
\end{array}\right]
$$

##### Example

If we want to shift all of the points in the plane by 2 units in the $x$-direction and
3 units in the $y$-direction, then

$$
T = \left[\begin{array}{c}
      2 \\
      3 \\
    \end{array}\right].
$$

#### Rotations

To calculate the position of any point $p = (x, y)$ in the plane after rotating by an angle
$\theta$ about the origin $(0, 0)$, we multiply the matrix representation of the point $p$
by the matrix $R$:

$$
R = \left[\begin{array}{cc}
      \cos \theta & -\sin \theta \\
      \sin \theta & \cos \theta \\
    \end{array}\right],
$$

where $\cos \theta$ is the _cosine_ of the angle $\theta$ and $\sin \theta$ is the _sine_
of the angle $\theta$. There is a lot to know about cosines and sines, but all we need to
know for now is that we can compute these values using a calculator or computer (just be
sure to enter the angle in _radians_ instead of degrees).

The location of the point $p$ after rotating by $\theta$ is

$$
R \times p = \left[\begin{array}{cc}
               x \cos \theta - y \sin \theta \\
               x \sin \theta + y \cos \theta \\
             \end{array}\right].
$$

##### Example

If we want to rotate all of the points in the plane by $90^\circ$, then the rotation
matrix $R$ is

$$
R = \left[\begin{array}{c}
      0 & -1 \\
      1 &  0 \\
    \end{array}\right]
$$

because $\cos 90^\circ = 0$ and $\sin 90^\circ = 1$.

##### Exercises

4. Verify that the formula for $R \times p$.

5. Find the rotation matrix for rotating by an angle of $60^\circ$. For reference:

   $$
   \cos 60^\circ
   = \cos \frac{\pi}{3}
   = \frac{1}{2}
   $$

   $$
   \sin 60^\circ
   = \sin \frac{\pi}{3}
   = \frac{\sqrt{3}}{2}
   $$

#### Reflections

To calculate the position of any point $p = (x, y)$ in the plane after reflecting across
a line passing through the origin $(0, 0)$ that makes an angle $\theta$ with the positive
$x$-axis, we multiply the matrix representation of the point $p$ by the matrix $S$:

$$
S = \left[\begin{array}{cc}
      \cos 2 \theta & \sin 2 \theta \\
      \sin 2 \theta & -\cos 2 \theta \\
    \end{array}\right].
$$

If we only know the slope $m$ of the line, then we can get the angle $\theta$ using the
formula: $\theta = \arctan m$. As with cosines and sines, all we need to know for now is
that we can compute $\theta$ from $m$ values using a calculator or computer (don't forget
that the angle will be calculated in _radians_ instead of degrees).

The location of the point $p$ after reflecting across the line that makes an angle
$\theta$ with the positive $x$-axis is

$$
S \times p = \left[\begin{array}{cc}
               x \cos 2 \theta + y \sin 2 \theta \\
               x \sin 2 \theta - y \cos 2 \theta \\
             \end{array}\right].
$$

#### Example

If we want to reflection all of the points in the plane across the line that makes a
$90^\circ$ angle with the positive $x$-axis, then the reflection matrix $S$ is

$$
S = \left[\begin{array}{c}
      -1 & 0 \\
       0 & 1 \\
    \end{array}\right]
$$

because $\cos 180^\circ = -1$ and $\sin 180^\circ = 0$.

### Exercises

6. Verify that the formula for $S \times p$.

7. Find the reflection matrix for reflecting across the line that makes a $60^\circ$ angle
   with the positive $x$-axis. For reference:

   $$
   \cos 120^\circ
   = \cos \frac{2 \pi}{3}
   = -\frac{1}{2}
   $$

   $$
   \sin 120^\circ
   = \sin \frac{2 \pi}{3}
   = \frac{\sqrt{3}}{2}
   $$

### Challenge Problems

8. Find a matrix formula for the location of a point $p$ after the following multi-step
   transformation of the plane.

   * First, rotate by an angle $\theta$.

   * Then, reflect across a line that makes an angle $\phi$ with the positive $x$-axis.

   * Finally, translate by $\Delta x$ in the $x$-direction and $\Delta y$ in the
     $y$-direction.

--------------------------------------------------------------------------------------------

## Resources

* [Hints](UZeo2oZpVHB988NvkP3eRa-hints.md)
* [Solutions](UZeo2oZpVHB988NvkP3eRa-solutions.md)

--------------------------------------------------------------------------------------------

* _Puzzle ID_: UZeo2oZpVHB988NvkP3eRa
* _Puzzle Version_: 2022-09-11T16:57:45
