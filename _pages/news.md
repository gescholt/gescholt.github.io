---
layout: page
title: news
permalink: /news/
description: a list of news and announcements
nav: false
nav_order: 6
---

<div class="news">
  {% assign news = site.news | reverse %}
  {% for item in news %}
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
  {% endfor %}
</div>