---
layout: post
permalink: /globtim/trefethen_function/
title: Trefethen Function
date: 2024-09-18
---

Here we consider the Trefethen function from the Problem 4 of the [100 Digit challenge](https://en.wikipedia.org/wiki/Hundred-dollar,_Hundred-digit_Challenge_problems).

$$ f(x, y) = \exp(\sin(50 x)) + \sin(60 \exp(y)) + \sin(70 \sin(x)) + \sin(\sin(80 y)) - \sin(10 (x + y)) + (x^2 + y^2) / 4 $$

This function has about $$2720$$ critical points in $$ [-1, 1]^2 $$, which is slightly too much for us, at least for the moment, hence we subdivide the domain.

<iframe src="/assets/plotly/Trefethen/trefethen_function_plot.html" width="100%" height="800px" frameborder="0"></iframe>

Here is the output of the critical points we are able to compute on the domain $$ [-.2, .2]^2 $$ with a polynomial approximant of degree 25.
