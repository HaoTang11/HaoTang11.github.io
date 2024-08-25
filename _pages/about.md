---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am now a master student in the [Shenzhen Institute of advanced technology](https://szs.siat.ac.cn/#/), Chinese Academy of science (中科院深圳先进技术研究院数字所）, mainly engaged in the research of computer vision  pose estimation and imitation learning.

I graduated from College of Intelligent Systems Science and Engineering, [Harbin engineering university](https://cisse.hrbeu.edu.cn/) (哈尔滨工程大学智能科学与工程学院) with a bachelor’s degree. Now, I’m pursuing my master’s degree in University of Chinese Academy of Science (中国科学院大学), advised by [Chang Liu](https://dblp.uni-trier.de/pid/52/5716-9.html) (刘畅).

My research interest includes visual navigation, pose tracking and state estimation. I have submitted 4 papers in EI/SCI journals, and attended 1 EI conference.

# 📖 Educations
- 2022.09 - current, Harbin Institute of Technology, Beijing/Shenzhen, (Score: 3.82/4.00)
- 2018.09 - 2022.06, Harbin Engineering University, Harbin, (GPA: 92.44/100, rank: top 3%)

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based pose tracking</div><img src='images/paper1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Model-based monocular 6-degree-of-freedom pose tracking for asteroid](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1337262/full)

**Hao Tang**, Chang Liu* (supervisor), Yuzhu Su, Qiuyin Wang, Weiduo Hu

[**Paper**](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1337262/full)
- we propose a robust 2D-3D correspondence method based on the covariance of the pose.
- we determine the asteroid pose by minimizing the angles between the projection planes of the extracted 3D contour segments and the back-projection lines of the corresponding 2D edge points.
- we infer the covariance matrix of the estimated pose based on the first-order optimality of the pose optimization.
- we use 2nd-AR-based SCKF to give the final pose estimate and initialize the pose tracking at the next time instant. 
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based pose tracking</div><img src='images/paper2.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Model-based visual 3D pose tracking of non-cooperative spacecraft in Close Range](https://iafastro.directory/iac/paper/id/77170/summary/)

Chang Liu*, **Hao Tang**

**Paper**
- automatic extraction and parametrization for the 3D boundaries and 3D contour of a spacecraft
- data correspondence based on truncated gaussian distribution
- real-time pose determination based on minimization of segment-to-line distance
- the first-order inference to covariance matrix of the estimated pose.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based pose tracking</div><img src='images/paper3.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Real-time Monocular 3D Pose Tracking for Non-cooperative Spacecraft in Close Range

**Hao Tang**, Chang Liu*, Jia Liu, Pandeng Zhang, Weiduo Hu 

**Paper**
- automatic extraction and parametrization for the 3D boundaries and 3D contour of a spacecraft
- data correspondence based on truncated gaussian distribution
- real-time pose determination based on minimization of segment-to-line distance
- the first-order inference to covariance matrix of the estimated pose.
- automatic extraction and parameterization of the geometric features (arbitrary 3D boundaries and contour) given the spacecraft mesh model
- 2D-3D correspondence based on conditional linear random field
- real-time pose estimation in SE(3) based on Newton method
- first-order pose covariance inference based on Cartesian noise model
-  ESKF based on second-order autoregression in SE(3)
</div>
</div>


# 🎖 Honors and Awards
- 2024.05	Merit Student Award (top 3%), University of Chinese Academy of Science, China
- 2023.03	Outstanding student award (top 5%), Shenzhen Institute of Advanced Technology, China
- 2022.06	Graduation Thesis Awards (top 1%), Harbin Engineering University, China
- 2022.06	Outstanding Graduate (top 3%), Harbin Engineering University, China
- 2021.10	National Scholarship (top 1%), Ministry of Education, China
- 2021.10	1st Prize (top 3%), Ti Cup National Undergraduate Electronic Design Contest, China
- 2020.12	3rd Prize (top 15%), The Chinese Mathematics Competitions, China
- 2020.10	3rd Prize (top 10%), China Undergraduate Mathematical Contest in Modeling, China
- 2020.08	1st Prize (top 5%), Mathematical modeling of the three northeastern provinces League, China

# 💬 Invited Talks
- *2023.10*, H. Tang. Model-based visual 3D pose tracking of non-cooperative spacecraft in Close Range, the 74th International Astronautical Congress, Baku, Azerbaijan, October 2023. (invited speaker)

# 💻 Internships
- *2023.06-2023.08*, Java Developer (full-time intern), Huawei Technologies Co. Ltd., China
