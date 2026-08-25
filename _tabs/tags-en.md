---
layout: page
title: Tags
icon: fas fa-tags
order: 2
lang: en
permalink: /en/tags/
alternate_url: /tags/
---

<div id="tags" class="d-flex flex-wrap mx-xl-2">
{% for item in site.data.writing %}
  {% assign copy = item.en %}
  {% for tag in copy.tags %}
  <div id="{{ tag | slugify }}">
    <a class="tag" href="{{ copy.url | relative_url }}">{{ tag }} <span class="text-muted">1</span></a>
  </div>
  {% endfor %}
{% endfor %}
</div>
