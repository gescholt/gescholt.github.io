---
layout: page
permalink: /globtim/
title: Globtim
date: 2024-08-07
nav: true
nav_order: 4
---

Globtim is a Julia package for solving global optimization problems via polynomial approximations.

For this method to work, we only require access to evaluations of the objective function `f`.

We call this method global because we seek to compute all local minima of the objective function `f`, a real continuous function defined over some
given rectangular domain in $$\\R^n$$.

Our method is carried out in 3 main steps:

1. The input function `f` is sampled on a tensorized Chebyshev grid
2. A polynomial approximant is constructed via a discrete least squares
3. The polynomial system of Partial derivatives is solved by either homotopy continuation (numerical method) or through exact polynomial system
   solving (symbolic method)

## Example

Here we consider the Trefethen function from Problem 4 of the
[100 Digit Challenge](https://en.wikipedia.org/wiki/Hundred-dollar,_Hundred-digit_Challenge_problems).

$$
f(x, y) = \exp(\sin(50x_1)) + \sin(60\exp(x_2)) + \sin(70\sin(x_1)) + \sin(\sin(80x_2)) - \sin(10(x_1 + x_2)) + \frac{x_1^2 + x_2^2}{4}
$$

We restrict the approximation to a square subdomain of $$[-1, 1]^2$$ of side length $$1/3$$. The orange points are the critical points of a
least-squares polynomial approximant of degree $$14$$ computed on a Chebyshev grid of $$1600$$ points.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/polyapprox_rotation.mp4" 
                      class="img-fluid rounded z-depth-1"
                      controls=true
                      autoplay=true
                      muted=true
                      loop=true %}
    </div>
</div>
