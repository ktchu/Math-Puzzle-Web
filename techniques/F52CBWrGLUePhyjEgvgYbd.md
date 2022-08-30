---
id: F52CBWrGLUePhyjEgvgYbd
title: Telescoping Series
tags: telescoping-series
---

--------------------------------------------------------------------------------------------

## Telescoping Series

_Telescoping series_ are sums with terms (in parenthesis) that look like the following:

$$
(a - b) + (b - c) + (c - d) + \cdots + (x - y) + (y - z).
$$

Rearranging the parenthesis, this sum is equal to

$$
a + (-b + b) + (-c + c) + (-d + d) + \cdots + (-x + x) + (-y + y) - z.
$$

Since all of the terms in the middle cancel out, the sum _collapses_ to

$$
a - z.
$$

It usually takes some effort to recognize that a sum is a telescoping series, but once you
do, calculating the sum becomes trivial!

### Example

Suppose we want to calculate the value of the sum

$$
S = \frac{1}{2} + \frac{1}{6} + \frac{1}{12} + \cdots + \frac{1}{9,900}
$$

If we play around with terms, we might notice that each term is of the form

$$
\frac{1}{n(n+1)}.
$$

For instance, $1/2 = 1/(1 \times 2)$, $1/6 = 1/(2 \times 3)$, and so on. Playing around
with this fraction a little more, we might recognize that

$$
\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}.
$$

Using this form for each term, the original sum becomes

$$
S = \left(\frac{1}{1} - \frac{1}{2}\right)
  + \left(\frac{1}{2} - \frac{1}{3}\right)
  + \left(\frac{1}{3} - \frac{1}{4}\right)
  + \cdots
  + \left(\frac{1}{99} - \frac{1}{100}\right),
$$

which collapses to $1 - 1/100 = 99/100$.

### Exercises

1. Use the idea of a telescoping series to derive the formula for a geometric series:

   $$
   S = a + a r + a r^2 + \cdots + a r^n.
   $$

[Solutions](F52CBWrGLUePhyjEgvgYbd-solutions.md)

--------------------------------------------------------------------------------------------

* _Puzzle ID_: F52CBWrGLUePhyjEgvgYbd
* _Puzzle Version_: 2022-08-30
