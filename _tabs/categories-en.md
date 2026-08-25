---
layout: page
title: Categories
icon: fas fa-stream
order: 1
lang: en
permalink: /en/categories/
alternate_url: /categories/
---

{% for item in site.data.writing %}
  {% assign copy = item.en %}
  {% for category in copy.categories %}
  <div id="{{ category | slugify }}" class="card categories mb-3">
    <div class="card-header">
      <i class="far fa-folder fa-fw"></i>
      <strong class="mx-2">{{ category }}</strong>
      <span class="text-muted small">1 post</span>
    </div>
    <div class="card-body py-3">
      <a href="{{ copy.url | relative_url }}">{{ copy.title }}</a>
    </div>
  </div>
  {% endfor %}
{% endfor %}
