---
layout: default
title: Teaching
permalink: /teaching/
---

<h2>Teaching</h2>

<ul>
{% assign items = site.teaching | sort: 'term' | reverse %}
{% for item in items %}
  <li>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
    <span class="meta">{% if item.course %} · {{ item.course }}{% endif %}{% if item.term %} · {{ item.term }}{% endif %}{% if item.role %} · {{ item.role }}{% endif %}</span>
  </li>
{% endfor %}
</ul>


