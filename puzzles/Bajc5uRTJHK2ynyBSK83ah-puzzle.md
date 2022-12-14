---
id: Bajc5uRTJHK2ynyBSK83ah
title: Squaring Two-Digit Numbers in Your Head
version: 2022-08-13
tags: algebra, geometry, mental-math
---

--------------------------------------------------------------------------------------------

## Squaring Two-Digit Numbers in Your Head

Here is a trick for squaring a two-digit number $x$ in your head.

* Find nearest multiple of 10 to $x$. Call that number $a$. Remember the difference $d$
  between $x$ and $a$ (ignore the sign).

* If you moved up to find the nearest multiple of 10, calculate $x - d$. Call that
  number $b$.

* If you moved down to find the nearest multiple of 10, calculate $x + d$. Call that
  number $b$.

* Multiply $b$ and $a$. Since $a$ is a multiple of 10, we only need to mulitply a two-digit
  number by a one-digit number in this step.

* Add $d^2$ to the result of the previous step. The final result is equal to $x^2$.

This trick is makes it easier to square numbers in your head because (1) you only have to
keep track of a couple of numbers at a time and (2) multiplying by multiples of 10 is easy.

__Example 1__. Calculate $19^2$.

* The nearest multiple of 10 to 19 is 20, so $a = 20$. The difference between 20 and 19 is
  1 so $d = 1$.
* We went up to get from 19 to 20, so $b = 19 - 1 = 18$.
* Multiply 18 and 20 to get 360.
* Add $d^2 = 1^2 = 1$ to 360 to get the answer 361.

__Example 2__. Calculate $27^2$.

* The nearest multiple of 10 to 27 is 30, so $a = 30$. The difference between 30 and 27 is
  3 so $d = 3$.
* We went up to get from 27 to 30, so $b = 27 - 3 = 24$.
* Multiply 24 and 30 to get 720.
* Add $d^2 = 3^2 = 9$ to 720 to get the answer 729.

__Example 3__. Calculate $74^2$.

* The nearest multiple of 10 to 74 is 70, so $a = 70$. The difference between 74 and 70 is
  4 so $d = 4$.
* We went down to get from 74 to 70, so $b = 74 + 4 = 78$.
* Multiply 78 and 70 to get 5460.
* Add $d^2 = 4^2 = 16$ to 5460 to get the answer 5476.

Draw a diagram of a square with side $x$ cut up into pieces that shows why this formula
works.

__Bonus__: Does this formula work when squaring numbers with more than two digits?

--------------------------------------------------------------------------------------------

## Resources

* [Hints](Bajc5uRTJHK2ynyBSK83ah-hints.md)
* [Solutions](Bajc5uRTJHK2ynyBSK83ah-solutions.md)

--------------------------------------------------------------------------------------------

* _Puzzle ID_: Bajc5uRTJHK2ynyBSK83ah
* _Puzzle Version_: 2022-08-13
