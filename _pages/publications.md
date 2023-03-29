---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="https://www.researchgate.net/profile/Yin-Zhang-36">my Google Scholar profile</a>.</u>

{% include base_path %}
(# equal contribution, * corresponding author)
<ol reversed>
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
</ol>
