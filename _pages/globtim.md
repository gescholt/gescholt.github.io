---
layout: post
permalink: /globtim/
title: Globtim
date: 2024-09-18
nav: true
nav_order: 4
---

[Globtim](https://github.com/gescholt/Globtim.jl) is a Julia package for solving global optimization problems via polynomial approximations.
It can be installed from the Julia REPL, simply by running the command

```julia
add Globtim
```

This global optimization method only requires access to evaluations of the objective function `f`.

We call this method global because we seek to compute all local minimizers of the objective function `f`, a real continuous function defined over some given rectangular domain in $$\mathbb{R}^n$$.

Our method is carried out in three main steps:

1. The input function `f` is sampled on a tensorized Chebyshev grid.
2. A polynomial approximant is constructed via a discrete least squares.
3. The polynomial system of Partial derivatives is solved with either a homotopy continuation method (numerical) or through an exact polynomial system solving (symbolic) method.

A comprehensive documentation for the package is actively worked on, for the time being, the following examples illustrate how the package can be used.

## Example

The following is the Deuflhard function, a standard example in Optimization:

$$
f(x, y) = \left( e^{x^2 + y^2} - 3 \right)^2 + \left( x + y - \sin(3(x + y)) \right)^2.
$$

It admits tow local maximizers and 6 local minimizers in the standard 2-cube.

### Exact evaluations

In the exact evaluation model, we will prioritize a high accuracy of the discrete least squares approximant over the number of samples we choose to generate.
The display of sample points and critical points can be turned **on/off** by clicking on them in the legend of the right top corner of the interactive plot.

<iframe src="/assets/plotly/Deuflhard/3d_Deuflhard.html" width="100%" height="1000px" frameborder="0"></iframe> <div style="text-align: center; margin-top: 10px;"> <strong>Legend:</strong> <span style="color: red;">Red - Critical Points of the polynomial approximant</span> </div>

Here the degree of the polynomial approximant is $12$ and the number of samples is.

### Noisy Evaluations

We now affect the evaluations of `f` by a Gaussian random noise of standard deviation 5.  
We can operate with a low tolerance and hope to get a very approximate location of the local minimizers of the function `f`.

<iframe src="/assets/plotly/Deuflhard/Deuflhard_low_tol.html" width="100%" height="1000px" frameborder="0"></iframe> <div style="text-align: center; margin-top: 10px;"> <strong>Legend:</strong> <span style="color: red;">Red - Critical Points of the exact polynomial approximant</span>
<span style="color: orange;">Orange - Critical Points of the noise perturbed polynomial approximant</span>
 </div>

Or we can move to a more precise setting which will lead to much more sample points generated, and a much more accurate estimate of the local minimizers of the objective function

<iframe src="/assets/plotly/Deuflhard/Deuflhard_high_tol.html" width="100%" height="1000px" frameborder="0"></iframe> <div style="text-align: center; margin-top: 10px;"> <strong>Legend:</strong> <span style="color: red;">Red - Critical Points of the exact polynomial approximant</span>
<span style="color: orange;">Orange - Critical Points of the noise perturbed polynomial approximant</span>
 </div>

## Additional examples

We provide two more examples on well known objective functions, this time with the detailed associated Julia code.

- [Camel Function](/globtim/camel_function/)
- [Trefethen Function](/globtim/trefethen_function/)
