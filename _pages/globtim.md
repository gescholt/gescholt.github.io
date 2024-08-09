
---
layout: page
permalink: /globtim/
title: Globtim
date: 2024-08-07
nav: true
nav_order: 5
---

Globtim is a Julia package for solving global optimization problems via polynomial approximations.

For this method to work, we only require access to evaluations of the objective function $f$.  

We call this method global because we seek to compute all local minima of the objective function `f`, a real continuous function defined over some given rectangular domain in $\\R^n$. 

Our method is carried out in 3 main steps:


1. The input function $f$ is sampled on a tensorized Chebyshev grid
2. A polynomial approximant is constructed via a discrete least squares
3. The polynomial system of Partial derivatives is solved by either homotopy continuation (numerical  method) or through exact polynomial system solving (symbolic method)

## Example

Here we consider the Trefethen function from the Problem 4 of the \[100 Digit challenge\](<https://en.wikipedia.org/wiki/Hundred-dollar,_Hundred-digit_Challenge_problems>). 

$$

f(x, y) = \\exp(\\sin(50  x\[1\])) + \\sin(60  \\exp(x\[2\])) + \\sin(70 \\sin(x\[1\])) + \\sin(\\sin(80 x\[2\])) - \\sin(10 (x\[1\] + x\[2\])) + (x\[1\]^2 + x\[2\]^2) / 4

$$

This function has about $2720$ critical pointsin $\[-1, 1\]^2$, which is slightly too much for us, at least for the moment, hence we subdivide the domain.  

<iframe src="/assets/plotly/trefethen_function_plot.html" width="100%" height="800px" frameborder="0"></iframe>