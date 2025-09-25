---
layout: default
title: Blog
permalink: /blog/
---

<h2>Blog</h2>

<div class="post-list">
{% for post in site.posts %}
  <article>
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <div class="meta">{{ post.date | date: '%b %d, %Y' }}</div>
    <p>{{ post.excerpt | strip_html | truncate: 180 }}</p>
  </article>
{% endfor %}
</div>



