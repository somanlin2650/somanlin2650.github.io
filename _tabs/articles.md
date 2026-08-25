---
layout: page
title: 文章
icon: fas fa-pen-nib
order: 0
---

<p>這裡收錄書籍之外的獨立文章。</p>

<div class="article-list">
{% for post in site.posts %}
  <article>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
    <p class="article-meta">{{ post.date | date: "%Y-%m-%d" }}</p>
  </article>
{% endfor %}
</div>

<style>
.article-list article {
  padding: 1.4rem 0 1.6rem;
  border-bottom: 1px solid var(--main-border-color);
}
.article-list article:first-child { padding-top: .5rem; }
.article-list h2 { margin: 0 0 .65rem; font-size: 1.35rem; line-height: 1.5; }
.article-list p { margin-bottom: .5rem; }
.article-list .article-meta { color: var(--text-muted-color); font-size: .85rem; }
</style>
