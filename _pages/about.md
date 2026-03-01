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

<!--I am now a master student in the [Shenzhen Institute of advanced technology](https://szs.siat.ac.cn/#/), Chinese Academy of science (中科院深圳先进技术研究院数字所).
I graduated from College of Intelligent Systems Science and Engineering, [Harbin engineering university](https://cisse.hrbeu.edu.cn/) (哈尔滨工程大学智能科学与工程学院) with a bachelor’s degree. Now, I’m pursuing my master’s degree in University of Chinese Academy of Science (中国科学院大学), advised by [Chang Liu](https://dblp.uni-trier.de/pid/52/5716-9.html) (刘畅).-->

# 👨‍💻 About Me
I am an **Autonomous Driving Engineer** at the **2030 LAB, Yinwang (Huawei Intelligent Automotive Solution BU)**. My work is dedicated to developing the next generation of autonomous driving systems, specifically focusing on:

  - **Foundation Models**: VLA/VLM, World Models

  - **End-to-End Autonomous Driving**: PV/BEV Perception, sensor fusion, trajectory planning, perception-action alignment

  - **AI Infra**: Memory Optimization, Streaming Inference, Token Compression

I earned my Master’s degree from the University of Chinese Academy of Sciences, where I conducted my research at the Shenzhen Institute of Advanced Technology. Prior to that, I received my Bachelor’s degree with honor from the College of Intelligent Systems Science and Engineering at Harbin Engineering University. My previous research expertise is deeply rooted in classical perception and state estimation, with a specific focus on 6-DoF pose tracking, multi-view geometry, SLAM, and recursive filtering for safety-critical localization.

I have published 2 peer-reviewed SCI journal papers (***IEEE TIM*** , ***MST***), and 3 EI conference papers (***CVPR***, ***MICCAI***, ***IAC***).  I am open for the opportunty of collaboration. Feel free to contact me if there's anything I can help you.

<span class='anchor' id='news'></span>

# 📢 News and updates
<div style="max-height: 250px; overflow-y: auto; padding: 10px; border: 1px solid #eee; border-radius: 5px;">
  <ul>
    <li><strong>[2026.02]</strong> Our paper (Percept-WAM) was accepted by CVPR 2026</li>
    <li><strong>[2025.10]</strong> Our paper (Monocular-vision-based) was accepted by MST</li>
    <li><strong>[2025.06]</strong> Joined 2030 LAB, Yinwang (Huawei IAS BU)</li>
    <li><strong>[2025.06]</strong> Our paper (Marker-less Head) was accepted by MICCAI 2025</li>
    <li><strong>[2025.04]</strong> Our paper (Real-time Monocular) was accepted by IEEE TIM</li>
    <li><strong>[2024.10]</strong> Create this website</li>
    <li><strong>[2023.02]</strong> Our paper (Model-based visual) was accepted by IAC</li>
    </ul>
</div>

<span class='anchor' id='educations'></span>

# 📖 Educations
- 2022.09 - 2025.06, MSc. Computer Technology, University of Chinese Academy of Science, China (GPA: 3.82/4.00, rank: top 3%)
- 2018.09 - 2022.06, BSc. Automation Engineering, Harbin Engineering University, China (GPA: 92.44/100, rank: top 3%)

<span class='anchor' id='publications'></span>

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">VLA model</div><img src='images/percept-wam.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Percept-WAM: Perception-Enhanced World-Awareness-Action Model for Robust End-to-End Autonomous Driving

Jianhua Han, ..., **Hao Tang**, ..., Hang Xu*

*Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2026, Accepted 

[**Paper**](https://arxiv.org/abs/2511.19221) [**Video**](https://www.youtube.com/watch?v=YLM0_YLPZxk&t=93s)
- unified 2D/3D tokenization (World-PV/BEV) for holistic scene understanding within a VLM
- grid-conditioned prediction with IoU-aware parallel decoding for dense object perception
- streaming inference via a memory-enabled recursive framework for temporal consistency
- action-centric alignment of PV, BEV, and ego-status through specialized World-Action tokens
- SOTA performance on nuScenes (perception) and NAVSIM (planning) benchmarks over diffusion and modular baselines
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based pose tracking</div><img src='images/mst.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Monocular-vision-based non-cooperative spacecraft tracking for close-proximity missions

**Hao Tang**, Chang Liu*, Qiuying Wang, Weiduo Hu

*Measurement Science and Technology*, 2025, Published

[**Paper**](https://iopscience.iop.org/article/10.1088/1361-6501/ae1a06/meta)
- offline extraction and parameterization of prominent 3D boundaries and contours from spacecraft mesh models
- 2D-3D correspondence established via local geometric similarity and intensity consistency without GPU-based rendering
- fast pose determination on SO(3) by minimizing segment-to-line distances using a Newton's method
- temporal state estimation and refinement via Cubature Kalman Filter (CKF) based on a CTRV motion model
- high-efficiency performance achieving 0.6°/0.5% pose tracking error and 0.002s processing time per frame
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based medical navigation</div><img src='images/paper4.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Marker-less Head Pose Tracking for Image-guided Cerebral Artery Navigation](https://link.springer.com/chapter/10.1007/978-3-032-05114-1_34)

Qiuyin Wang, Pandeng Zhang, Dewei Chen, **Hao Tang**, Chang Liu*, Jia Liu*

*International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI)*, 2025, Accepted

[**Paper**](https://papers.miccai.org/miccai-2025/paper/1763_paper.pdf) 
- 3D facial model construction from preoperative MRI data
- A thin-plate spline function (TPSF) description encoding local geometry of facial model
- Registeration between RGBD camera and the facial model by maximum weight matching
- Real-time pose tracking based on SCKF-ICP fusion
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based pose tracking</div><img src='images/paper3.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Real-time Monocular 3D Pose Tracking for Non-cooperative Spacecraft in Close Range

**Hao Tang**, Chang Liu*, Jia Liu, Pandeng Zhang, Weiduo Hu 

*IEEE Transactions on Instrumentation and Measurement*, 2025, Published 

[**Paper**](https://ieeexplore.ieee.org/abstract/document/11002620)
- automatic extraction and parameterization of the geometric features (arbitrary 3D boundaries and contour) given the spacecraft mesh model
- 2D-3D correspondence based on conditional linear random field
- real-time pose estimation in SE(3) based on Newton method
- first-order pose covariance inference based on Cartesian noise model
- ESKF based on second-order autoregression in SE(3)
</div>
</div>


<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based pose tracking</div><img src='images/paper1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Model-based monocular 6-degree-of-freedom pose tracking for asteroid](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1337262/full)

**Hao Tang**, Chang Liu* (supervisor), Yuzhu Su, Qiuyin Wang, Weiduo Hu

*Frontiers in Space Technologies*, Published 

[**Paper**](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1337262/full)
- we propose a robust 2D-3D correspondence method based on the covariance of the pose.
- we determine the asteroid pose by minimizing the angles between the projection planes of the extracted 3D contour segments and the back-projection lines of the corresponding 2D edge points.
- we infer the covariance matrix of the estimated pose based on the first-order optimality of the pose optimization.
- we use 2nd-AR-based SCKF to give the final pose estimate and initialize the pose tracking at the next time instant. 
</div>
</div> -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based pose tracking</div><img src='images/iac.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Model-based visual 3D pose tracking of non-cooperative spacecraft in Close Range](https://iafastro.directory/iac/paper/id/77170/summary/)

Chang Liu*, **Hao Tang**

*Proceedings of the 74th International Astronautical Congress (IAC)*, 2023, Published 

[**Paper**](https://www.engineeringvillage.com/app/doc/?docid=cpx_M6d3c13d618e770d7715M650410178165153&pageSize=25&index=1&searchId=a9df5555e93749cc9b9c6dc33dedf516&resultsCount=1&usageZone=resultslist&usageOrigin=searchresults&searchType=Quick)
- automatic extraction and parametrization for the 3D boundaries and 3D contour of a spacecraft
- data correspondence based on truncated gaussian distribution
- real-time pose determination based on minimization of segment-to-line distance
- the first-order inference to covariance matrix of the estimated pose.
</div>
</div>

<!--# 🔍 Projects-->

<span class='anchor' id='honors-and-awards'></span>

# 🎖️ Honors and Awards
- 2024.05	Merit Student Award (top 3%), University of Chinese Academy of Science, China
- 2023.03	Outstanding student award (top 5%), Shenzhen Institute of Advanced Technology, China
- 2022.06	Graduation Thesis Awards (top 1%), Harbin Engineering University, China
- 2022.06	Outstanding Graduate (top 3%), Harbin Engineering University, China
- 2021.10	**National Scholarship** (top 1%), Ministry of Education, China
- 2021.10	1st Prize (top 3%), Ti Cup National Undergraduate Electronic Design Contest, China
- 2020.12	3rd Prize (top 15%), The Chinese Mathematics Competitions, China
- 2020.10	3rd Prize (top 15%), China Undergraduate Mathematical Contest in Modeling, China
- 2020.08	1st Prize (top 5%), Mathematical modeling of the three northeastern provinces League, China

<span class='anchor' id='invited-talks'></span>

# 💬 Invited Talks
- *2023.10*, H. Tang. Model-based visual 3D pose tracking of non-cooperative spacecraft in Close Range, the 74th International Astronautical Congress, Baku, Azerbaijan, October 2023. (invited speaker)

<span class='anchor' id='internships'></span>

# 💻 Internships
***2023.06-2023.08*, Java Developer (full-time intern), Huawei Technologies Co. Ltd., China**
- Code version maintenance, including code testing, updating and security
- Code management for Huawei's corporate-level Code hosting services - Codehub, achieving 10,000+ response one day
- Development of key functions of Codehub for users, finishing a user-friendly search interface finally

***2023.09-2024.01*, TA (part-time), Shenzhen University of Advanced Technology, China**
- Course name: Matrix Theory, one of the major courses for undergraduate students
- Response to course related questions for 300+ students
