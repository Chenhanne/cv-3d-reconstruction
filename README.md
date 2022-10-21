# 3d-underwater-reconstruction

#### 介绍
computer vision 
3d-reconstruction
3d-underwater reconstruction

### 中文论文
- 刘舜; 徐亚楠 “	基于Retinex图像增强算法的水下三维重建研究” 工程勘察（2022）
- 钟志; 郑云天; 张扬; 孙岩; 王霖郁 “基于单目视觉的水下目标三维重建实验设计” 实验技术与管理 （2022）
- 庄苏锋; 屠大维; 张旭; 姚钦舟 “水下双目立体视觉对应点匹配与三维重建方法研究” 仪器表学报 （2022）
- 陈士杰; 张森林; 刘妹琴; 郑荣濠 “基于改进Delaunay三角剖分的水下地形三维重建算法” 计算机科学 （2020）
- 戴文文 “自主水下机器人回收对接中前景视场三维重建研究” 江苏科技大学 （2020）
- 王越 “基于双目视觉的水下环境三维重建” 哈尔滨工程大学 （2020）
- 赵子毅 “基于线结构光的深海小区域三维重建” 青岛科技大学 （2020）
- 许恒博; 杜金香 “基于声学图像的水下目标三维重建综述” 中国声学学会水声学分会2019年学术会议论文集 （2019）
- 张熠 “水下旋转扫描三维重建技术研究” 哈尔滨工程大学 （2019）
- 刘文静 “光度立体与结构光融合的水下三维重建” 青岛理工大学 （2018）
- 李冬平; 何雯; 高健 “利用水声纳稀疏条带测量数据进行水下地形三维重建方法” 科技创新导报 （2018）
- 乔金鹤 “基于双目立体视觉的水下三维重建技术研究” 哈尔滨工程大学 （2018）
- 李雪峰 “基于前视声呐的水下场景三维重建方法的研究” 沈阳理工大学 （2017）
- 董会; 孔倩倩; 温亚楠; 杨宇 “水下目标彩色三维重建方法研究” 光电技术应用 （2017）
- 王凯旋 “水下环境中基于双目立体视觉的三维重建算法” 燕山大学 （2017）
- 


### 数据集整理
#### MVS三维重建公开数据集整理

- 固定翼无人机数据集https://www.sensefly.com/education/datasets/
轻型固定观测公司sensefly公开的数据集，有RGB、多翼光谱、热红外。 

- 著名的摄影测量公司 Pix4d 的公开数据集https://cloud.pix4d.com/demo

- 著名的摄影测量公司Aigsoft的公开数据集https://www.agisoft.com/downloads/sample-data/

- 著名的开源项目Colmap所公开的数据集http://colmap.github.io/datasets.html

- 著名的开源库OpenMVG所提供的公开数据集https://github.com/openMVG/Image_datasets

- 瑞士一家生产固定翼测绘地图的公司公开的数据集https://wingtra.com/pping-drone-wingtraone/aerial-map-types/

- 著名的Arcgis公司的公开数据集https://doc.arcgis.com/en/drone2map/get-started/sample-data.htm
其中36张的大楼数据很经典

- 一个集，比较文物保护的公开数据https://openheritage3d.org/data
里面有RGB和激光雷达数据，有很多项目是RGB彩色数据的，但是大部分是提供数码相机，没有GPS或者RTK 

- 丹麦技术大学丹麦技术大学提供的公开数据集https://roboimagedata.compute.dtu.dk/?page_id=36
难能贵的是他们的结构光扫描数据作为，还有不同的光线提供的变化，价值小视场的MVS重建真的很不错

- 日本东北大学东北大学提供的公开数据集 http://www.aoki.ecei.tohoku.ac.jp/mvs/
是小价值重建，只有拍摄的猫和狗的模型，同时提供了真正的拍摄效果 

- 港科大开源的数据集，有建筑、大规模、近景等各类数据https://github/YoYo000/BlendedMVS 

- 开源代码：https://github.com/Atif-Anwer/UWKFusion 附带了它们自己的数据集
与其配套的论文和视频：
https://www.youtube.com/watch?v=E5GNbEN16uQ
https://ieeexplore.ieee.org/document/8000305
论文涵盖在论文文件夹中

- 水下拍摄的 Kinect 数据数据集
已经获得了一个完整的数据集，其中包括水下扫描的各种物体。Kinect 的 RGB 和 IR 摄像头的数据与 KinectToF 生成的点云一起被捕获，并以 Microsoft 的扩展事件文件 (XEF) 文件格式保存，可与 Kinect Studio 应用程序一起使用。该数据集在 GNU GPL 3.0 许可下公开可用，可从以下链接下载：

- 水下图像双谱重建
https://github.com/yangggzhang/Underwater-Image-Bispectrum-Reconstruction

- 水下受损图像重建
https://github.com/yangxuxuxu/underwater-image-reconstruction
