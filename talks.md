---
layout: default
title: Talks
permalink: /talks/
---

<h2>Talks</h2>

<ul>
{% assign items = site.talks | sort: 'date' | reverse %}
{% for item in items %}
  <li>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
    <span class="meta">{% if item.event %} · {{ item.event }}{% endif %}{% if item.location %} · {{ item.location }}{% endif %}{% if item.date %} · {{ item.date | date: '%b %d, %Y' }}{% endif %}</span>
  </li>
{% endfor %}
</ul>


