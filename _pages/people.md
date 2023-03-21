---
layout: archive
title: "People"
permalink: /people/
author_profile: true
---

{% include base_path %}

<img src='/images/profile2.jpg' width="300"><br>
## Dr. Yin Zhang
<a href="/cv/">Full CV</a>


### Education
* 2011.08-2015.07 &emsp;B.S. in Theoretical and Applied Mechanics, Peking University <br>Advisor: Prof. Ting Zhu
* 2015.08-2021.08 &emsp;Ph.D in Mechanical Engineering, Georgia Institute of Technology <br>Advisor: Prof. Huiling Duan

### Experience
* 2021.09-2023.01 &emsp;Postdoctoral Associate, Massachusetts Institute of Technology <br>Advisor: Prof. Ju Li
* 2023.01-now &emsp;&emsp;&ensp;Assistant Professor, Peking University

{% for post in site.people %}
  {% include archive-single.html %}
{% endfor %}

