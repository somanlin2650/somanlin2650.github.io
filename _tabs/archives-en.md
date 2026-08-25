---
layout: page
title: Archives
icon: fas fa-archive
order: 3
lang: en
permalink: /en/archives/
alternate_url: /archives/
---

<div id="archives" class="pl-xl-3">
  <time class="year lead d-block">2026</time>
  <ul class="list-unstyled">
  {% for item in site.data.writing %}
    {% assign copy = item.en %}
    <li>
      <span class="date day">{{ item.date | date: "%d" }}</span>
      <span class="date month small text-muted ms-1">/ {{ item.date | date: "%m" }}</span>
      <a href="{{ copy.url | relative_url }}">{{ copy.title }}</a>
    </li>
  {% endfor %}
  </ul>
</div>
