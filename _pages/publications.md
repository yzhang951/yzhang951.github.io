---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CMCF4W65KR"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-CMCF4W65KR');
</script>
You can also find my articles on my <a href="https://scholar.google.com/citations?user=23XDhOwAAAAJ&hl=en">Google Scholar</a> profile.
<br><a href="/tags/">Publications by Tags</a>

{% include base_path %}
(# equal contribution, * corresponding author)
<ol reversed>
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
</ol>
