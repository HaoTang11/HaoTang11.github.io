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

I am now a master student in the [Shenzhen Institute of advanced technology](https://szs.siat.ac.cn/#/), Chinese Academy of science (中科院深圳先进技术研究院数字所).

I graduated from College of Intelligent Systems Science and Engineering, [Harbin engineering university](https://cisse.hrbeu.edu.cn/) (哈尔滨工程大学智能科学与工程学院) with a bachelor’s degree. Now, I’m pursuing my master’s degree in University of Chinese Academy of Science (中国科学院大学), advised by [Chang Liu](https://dblp.uni-trier.de/pid/52/5716-9.html) (刘畅).

My research interest includes visual navigation, pose tracking and state estimation. I have submitted 4 papers in EI/SCI journals, and attended 1 EI conference.

# 📖 Educations
- 2022.09 - current, University of Chinese Academy of Science, Beijing+Shenzhen, (Score: 3.82/4.00)
- 2018.09 - 2022.06, Harbin Engineering University, Harbin, (GPA: 92.44/100, rank: top 3%)

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based pose tracking</div><img src='images/paper3.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Real-time Monocular 3D Pose Tracking for Non-cooperative Spacecraft in Close Range

**Hao Tang**, Chang Liu*, Jia Liu, Pandeng Zhang, Weiduo Hu 

IEEE Transactions on Instrumentation and Measurement

[**Paper**](https://ieeexplore.ieee.org/abstract/document/11002620)
- automatic extraction and parameterization of the geometric features (arbitrary 3D boundaries and contour) given the spacecraft mesh model
- 2D-3D correspondence based on conditional linear random field
- real-time pose estimation in SE(3) based on Newton method
- first-order pose covariance inference based on Cartesian noise model
- ESKF based on second-order autoregression in SE(3)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based pose tracking</div><img src='images/paper1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Model-based monocular 6-degree-of-freedom pose tracking for asteroid](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1337262/full)

**Hao Tang**, Chang Liu* (supervisor), Yuzhu Su, Qiuyin Wang, Weiduo Hu

Frontiers in Space Technologies

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

Proceedings of the 74th International Astronautical Congress

[**Paper**](https://www.engineeringvillage.com/app/doc/?docid=cpx_M6d3c13d618e770d7715M650410178165153&pageSize=25&index=1&searchId=a9df5555e93749cc9b9c6dc33dedf516&resultsCount=1&usageZone=resultslist&usageOrigin=searchresults&searchType=Quick)
- automatic extraction and parametrization for the 3D boundaries and 3D contour of a spacecraft
- data correspondence based on truncated gaussian distribution
- real-time pose determination based on minimization of segment-to-line distance
- the first-order inference to covariance matrix of the estimated pose.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Vision-based medical navigation</div><img src='images/paper4.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Local Thin Plate Spline Descriptor for Aiding Marker-less Cerebral Artery Navigation Based on 3D Point Cloud Registration

Qiuyin Wang, Chang Liu*, **Hao Tang**

IEEE Transactions on Medical Imaging, under review

[**Part of Paper**](https://github.com/HaoTang11/Working_Set/blob/main/%E4%BD%9C%E5%93%81%E9%9B%86/Local%20Thin%20Plate%20Spline%20Descriptor%20for%20Aiding%20Marker-less%20Cerebral%20Artery%20Navigation%20Based%20on%203D%20Point%20Cloud%20Registration/%E8%AE%BA%E6%96%87%E9%83%A8%E5%88%86.pdf)
- A robust local reference frame with scaling strategy
- A local invariant point cloud descriptor is proposed based on thin plate spline
- A feature matching algorithm is improved based on fully connected CRF with geometric constraints
- The proposed descriptor and registration algorithm are applied to stimulation and real-world scenarios captured by depth camera and MRI images
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">pose initialization</div><img src='images/paper5.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

A Robust Template-based 3D Pose Initialization for Spacecraft by 2D Contour optimization

 **Hao Tang**, Chang Liu*

under research

**Paper**

The initial value of pose is crucial in the process of target tracking. This work mainly uses the template library generated by the target CAD model to estimate the initial pose of the target monocular image sequence. Compared with traditional template matching algorithms, our method does not rely on the PNP algorithm, require a smaller template library, exhibits greater robustness, and achieves higher estimation accuracy. 

Specifically, we improve the neural network SFSnet to segment the spacecraft from the input image and match the segmentation result (the 2D contour) of the input image with the binary image template library. We then apply the low-frequency information extracted by Fourier analysis of the 2D contour and Gaussian Mixture Model (GMM) to calculate the 2D pose and scaling factor between the input image and the template image. These parameters are used to derive a closed-form solution for the 3D pose, which serves as the initial estimate for a nonlinear optimization algorithm to further refine the pose estimation. Finally, we employ a Hidden Markov Model to optimize the pose estimation from several neareast neighboring solution and obtain the final pose.
</div>
</div>


# 🔍 Projects



# 🎖 Honors and Awards
- 2024.05	Merit Student Award (top 3%), University of Chinese Academy of Science, China
- 2023.03	Outstanding student award (top 5%), Shenzhen Institute of Advanced Technology, China
- 2022.06	Graduation Thesis Awards (top 1%), Harbin Engineering University, China
- 2022.06	Outstanding Graduate (top 3%), Harbin Engineering University, China
- 2021.10	National Scholarship (top 1%), Ministry of Education, China
- 2021.10	1st Prize (top 3%), Ti Cup National Undergraduate Electronic Design Contest, China
- 2020.12	3rd Prize (top 15%), The Chinese Mathematics Competitions, China
- 2020.10	3rd Prize (top 15%), China Undergraduate Mathematical Contest in Modeling, China
- 2020.08	1st Prize (top 5%), Mathematical modeling of the three northeastern provinces League, China

# 💬 Invited Talks
- *2023.10*, H. Tang. Model-based visual 3D pose tracking of non-cooperative spacecraft in Close Range, the 74th International Astronautical Congress, Baku, Azerbaijan, October 2023. (invited speaker)

# 💻 Internships
***2023.06-2023.08*, Java Developer (full-time intern), Huawei Technologies Co. Ltd., China**
- Code version maintenance, including code testing, updating and security
- Code management for Huawei's corporate-level Code hosting services - Codehub, achieving 10,000+ response one day
- Development of key functions of Codehub for users, finishing a user-friendly search interface finally

***2023.09-2024.01*, TA (part-time), Shenzhen University of Advanced Technology, China**
- Course name: Matrix Theory, one of the major courses for undergraduate students
- Response to course related questions for 300+ students
