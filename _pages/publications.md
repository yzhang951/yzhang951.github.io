---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on my <u><a href="https://scholar.google.com/citations?user=23XDhOwAAAAJ&hl=en">Google Scholar</a></u> profile.

<br><a href="/pub-tags/">Publications by Tags</a>

{% include base_path %}
(# equal contribution, * corresponding author)
<ol reversed>
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
</ol>
