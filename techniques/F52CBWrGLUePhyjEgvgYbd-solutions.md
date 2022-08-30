---
id: F52CBWrGLUePhyjEgvgYbd
title: Telescoping Series [Solutions]
tags: solutions
---

--------------------------------------------------------------------------------------------

## Telescoping Series [Solutions]

1. A geometric series can be calculated by converting the sum into a telescoping series.
Suppose we want to compute the geometric sum:

$$
S = 1 + r + r^2 + \cdots + r^9.
$$

Unfortunately, this is not a telescoping series. But it is _close_ to one! If we subtract
$S$ multiplied by $r$ from $S$, we get

$$
S - rS = (1 + r + r^2 + \cdots + r^9) - (r + r^2 + r^3 + \cdots + r^10).
$$

Combining corresponding terms in sums in the parenthesis, we get

$$
S - rS = (1 - r) + (r - r^2) + \cdots + (r^9 - r^{10}),
$$

which collapses to $1 - r^{10}$. Solving for $S$, we arrive at the formula

$$
S = \frac{1 - r^{10}}{1 - r}
$$

--------------------------------------------------------------------------------------------

* _Puzzle ID_: F52CBWrGLUePhyjEgvgYbd
* _Solutions Version_: 2022-08-30
