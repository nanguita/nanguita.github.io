---
layout: default
title: Publications
permalink: /publications/
---

<h2>Publications</h2>

<ul>
{% assign pubs = site.publications | sort: 'year' | reverse %}
{% for pub in pubs %}
  <li>
    <a href="{{ pub.url | relative_url }}">{{ pub.title }}</a>
    <span class="meta">{% if pub.authors %} · {{ pub.authors }}{% endif %}{% if pub.venue %} · {{ pub.venue }}{% endif %}{% if pub.year %} · {{ pub.year }}{% endif %}</span>
  </li>
{% endfor %}
</ul>


