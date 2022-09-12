---
id: RciLUwtYwZqqQZShTeX6Au
title: Collapsing Circular Sums
version: TBD
tags: trigonometry, telescoping-series
upstream: oRBnohfiqJq7zaWHjQBcmL, RQZXTKug9ZnB7dnetSGsNu
---

--------------------------------------------------------------------------------------------

## Collapsing Circular Sums

__TODO__

Calculate the following sums.

1.
$$
  \cos \left(\frac{\pi}{100} \right) + \cos \left(\frac{3\pi}{100} \right)
  + \cdots
  + \cos \left(\frac{97\pi}{100} \right)
$$

2.
$$
\begin{align}
\exp\left( \frac{i \theta}{n+1} \right) - \exp\left( \frac{i \theta}{n} \right)
&= \exp\left(\frac{i \theta}{n+1}\right)
   \left(1 - \exp\left( \frac{i \theta}{n(n+1)} \right) \right) \\
&= \exp\left(\frac{i \theta}{n+1}\right)
   \exp\left(\frac{i \theta}{2n(n+1)}\right)
   \left( \exp\left( \frac{-i \theta}{2n(n+1)} \right) 
        - \exp\left( \frac{i \theta}{2n(n+1)} \right) \right) \\
&= -2 i \sin \left( \frac{i \theta}{2n(n+1)} \right)
   \exp\left(\frac{i \theta}{n+1}\right)
   \exp\left(\frac{i \theta}{2n(n+1)}\right)
\end{align}
$$

### Bonus

A. If $n$ and $m$ are positive integers, what are the values of the following sums?
### Bonus

A. If $n$ and $m$ are positive integers, what are the values of the following sums?

   $$
     \cos \frac{2 \pi}{n} + \cos \frac{4 \pi}{n} + \ldots + \cos \frac{2(n - 1) \pi}{n}
   $$

   $$
     \sin \frac{2 \pi}{n} + \sin \frac{4 \pi}{n} + \ldots + \sin \frac{2(n - 1) \pi}{n}
   $$

--------------------------------------------------------------------------------------------

## Resources

* [Hints](RciLUwtYwZqqQZShTeX6Au-hints.md)
* [Solutions](RciLUwtYwZqqQZShTeX6Au-solutions.md)

--------------------------------------------------------------------------------------------

* _Puzzle ID_: RciLUwtYwZqqQZShTeX6Au
* _Puzzle Version_: TBD
* _Upstream_: [[oRBnohfiqJq7zaWHjQBcmL]], [[RQZXTKug9ZnB7dnetSGsNu]]
