---
layout: default
title: Portfolio
permalink: /portfolio/
---

<h2>Projects</h2>

<ul>
{% for item in site.portfolio %}
  <li>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
    <span class="meta">{% if item.tags %} · {{ item.tags | join: ', ' }}{% endif %}</span>
  </li>
{% endfor %}
</ul>


