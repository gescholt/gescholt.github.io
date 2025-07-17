---
layout: about
title: Georgy Scholten
permalink: /
# subtitle: 

profile:
  align: right
  image: profile.jpg
  image_circular: false # crops the image to make it circular
  address: >
    <p>Center for Systems Biology Dresden </p>
    <p>Pfotenhauerstr. 108</p>
    <p>01307 Dresden Germany</p>

news: false  # includes a list of news items
latest_posts: false  # includes a list of the newest posts
selected_papers: false # includes a list of papers marked as "selected={true}"
social: true  # includes social icons at the bottom of the page
---

I am currently at the [Center for Systems Biology Dresden](https://www.csbdresden.de/), where I am a postdoctoral researcher part of the [Harrington Group](https://www.mpi-cbg.de/research/researchgroups/currentgroups/heather-harrington/group).
Previously, I was a postdoc at [Sorbonne Université](https://www.sorbonne-universite.fr/en), jointly in the [Polsys](https://www-polsys.lip6.fr/) team and at the [Laboratoire Jacques-Louis Lions](https://www.ljll.math.upmc.fr/).
I completed my PhD in Mathematics under the supervision of [Dr. Cynthia Vinzant](https://sites.math.washington.edu/~vinzant/) in May 2021.

## News

{% assign news = site.news | reverse %}
{% for item in news limit:5 %}
<div class="news">
  <div class="row">
    <div class="col-sm-2 abbr">
      <span class="badge font-weight-bold danger-color-dark text-uppercase align-middle">
        {{ item.date | date: "%b %Y" }}
      </span>
    </div>
    <div class="col-sm-10">
      {{ item.content }}
    </div>
  </div>
</div>
{% endfor %}

My primary work involves studying mathematical structures that emerge from the study of dynamic and biological systems.
A central motivation in my research is to combine symbolic and numerical methods in a best of both worlds approach, in order to enhance methods in optimization and statistical analysis which can be leveraged in various interdisciplinary settings.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        <video class="video-fluid w-100" controls>
            <source src="{{ site.baseurl }}/assets/video/level_set_animation.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
</div>
<div class="caption">
    Level sets of the Trefethen 3d function:
\begin{align}
f(x, y, z) = e^{\sin(50x_1)} + \sin(60e^{x_2})\sin(60x_3) + \sin(70\sin(x_1))\cos(10x_3) \\
+ \sin(\sin(80x_2)) - \sin(10(x_1 + x_3)) + \frac{x_1^2 + x_2^2 + x_3^2}{4}
\end{align}
</div>
The locations of the critical points have been computed using the [Globtim package]({% link _pages/globtim.md %}).