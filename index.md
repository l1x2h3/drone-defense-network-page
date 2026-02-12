---
title: 无人机防御网络系统
layout: home
nav_order: 1
description: 基于SDR与AI的智能无人机防御平台
---

<style>
  .feature-card {
    background: #f8f9fa;
    border-left: 4px solid #0d6efd;
    padding: 1.2rem;
    margin: 1.5rem 0;
    border-radius: 0 4px 4px 0;
  }
  .section-header {
    border-bottom: 1px solid #eaecef;
    padding-bottom: 0.4rem;
    margin-top: 2rem;
    margin-bottom: 1.2rem;
  }
  .highlight-box {
    background-color: #fff8e1;
    padding: 1rem;
    border-radius: 4px;
    margin: 1rem 0;
  }
  .tech-flow {
    display: flex;
    flex-wrap: wrap;
    gap: .7rem;
    align-items: center;
    margin: 1rem 0 1.4rem;
  }
  .flow-node {
    padding: .55rem .85rem;
    font-weight: 600;
    color: #0b3d91;
    background: #eef4ff;
    border: 1px solid #b8d0ff;
    text-align: center;
    min-width: 90px;
  }
  .shape-rect { border-radius: 6px; }
  .shape-round { border-radius: 999px; }
  .shape-diamond {
    width: 84px;
    height: 84px;
    min-width: unset;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transform: rotate(45deg);
    border-radius: 8px;
  }
  .shape-diamond span { transform: rotate(-45deg); display: inline-block; }
  .shape-parallelogram {
    transform: skewX(-15deg);
    border-radius: 4px;
  }
  .shape-parallelogram span { display: inline-block; transform: skewX(15deg); }
  .flow-arrow {
    color: #6b7280;
    font-weight: 700;
    font-size: 1.1rem;
  }
  .principle-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: .9rem;
    margin-top: .8rem;
  }
  .principle-card {
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: .85rem .9rem;
    background: #ffffff;
    box-shadow: 0 1px 2px rgba(0, 0, 0, .04);
  }
  .principle-card h4 {
    margin: 0 0 .45rem;
    font-size: 1rem;
  }
  .principle-card p {
    margin: .25rem 0;
    font-size: .92rem;
    line-height: 1.5;
  }
  .layer-stack {
    max-width: 860px;
    margin: 1rem auto 1.4rem;
    border: 1px solid #d9e2f2;
    border-radius: 10px;
    overflow: hidden;
    background: #ffffff;
  }
  .layer-row {
    padding: .75rem 1rem;
    text-align: center;
    font-weight: 600;
    border-top: 1px solid #e8edf7;
    background: linear-gradient(180deg, #f9fbff 0%, #f2f6ff 100%);
  }
  .layer-row:first-child {
    border-top: 0;
  }
  .layer-row em {
    font-style: normal;
    font-weight: 500;
    color: #4b5563;
    margin-left: .3rem;
  }
  .flow-board {
    max-width: 980px;
    margin: 1rem auto 1.4rem;
    display: grid;
    gap: .55rem;
  }
  .flow-line {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: .45rem;
  }
  .flow-box {
    background: #ffffff;
    border: 1px solid #dbe4f3;
    border-radius: 8px;
    padding: .45rem .7rem;
    font-size: .92rem;
    font-weight: 600;
    color: #1f2937;
  }
  .flow-box.core {
    background: #edf4ff;
    border-color: #bfd4ff;
    color: #0b3d91;
  }
  .flow-connector {
    color: #64748b;
    font-weight: 700;
    line-height: 1;
    padding: 0 .1rem;
  }
  .flow-line.offset-left {
    margin-left: 1.8rem;
  }
  .flow-line.offset-right {
    margin-left: 9.2rem;
  }
</style>


# 无人机防御网络系统  
**基于SDR与AI的智能电磁感知与精准反制平台**  

<div class="highlight-box">
  <p>🚀 <strong>系统概述</strong>：本系统是业界首套将软件定义无线电（SDR）、深度学习、高精度定位与自适应干扰技术深度融合的智能安防平台。采用“侦—识—定—扰—评”五维闭环架构，从电磁频谱感知到多手段协同反制，实现全天候、全频段、全协议的低空无人机防御，关键技术指标达到国际先进水平。</p>
</div>

---

## 🔧 核心功能

<div class="feature-card">
  <strong>📡 全频段频谱侦测</strong><br>
  覆盖 20 MHz – 6 GHz，兼容 DJI OcuSync、Autel、Parrot、Skydio、WiFi 2.4/5.8 GHz、蓝牙、4G/5G 及 MAVLink 等主流协议。支持瞬态信号捕获与跳频模式识别，毫秒级频谱刷新。
</div>

<div class="feature-card">
  <strong>🧠 多模态信号智能识别</strong><br>
  融合射频指纹（RF Fingerprinting）、小波包分解、MFCC 及循环平稳特征，通过 CNN+SVM 混合模型实现 30+ 种无人机型号的实时分类，小样本迁移学习使新协议识别准确率 ≥92%。
</div>

<div class="feature-card">
  <strong>📍 TDOA+AOA 融合定位</strong><br>
  分布式 SDR 传感器节点通过 GPS 纳秒级同步，联合到达时间差（TDOA）与到达角度（AOA）算法，实现亚米级三维定位（误差 ≤3 m）。卡尔曼滤波轨迹预测，支持动态目标连续跟踪。
</div>

<div class="feature-card">
  <strong>⚡ 自适应智能干扰</strong><br>
  基于深度 Q 网络（DQN）动态优化干扰频率、带宽、功率与波束指向，支持宽带噪声压制、协议级欺骗（Deauth、GPS Spoofing）及图传链路阻断。干扰策略毫秒级切换，附带干扰效能自动评估。
</div>

<div class="feature-card">
  <strong>📹 计算机视觉辅助识别</strong><br>
  集成 YOLOv8 目标检测模型，GPU 加速推理（≥30 FPS），实时识别无人机类型并叠加检测框。视觉结果与雷达/频谱数据多模态融合，误报率降低 65%。
</div>

<div class="feature-card">
  <strong>🌐 远程设备管理与态势可视化</strong><br>
  基于阿里云 01-KICKPI-K2B 远程控制框架，实现 HackRF 等 SDR 设备的 SSH 远程操控，API 100% 兼容本地 pyhackrf。可视化界面包含电子地图、频谱热力图、设备拓扑及威胁轨迹回放，支持多屏联动。
</div>

<div class="feature-card">
  <strong>💥 多协议协同攻击平台</strong><br>
  一体化集成 WiFi 2.4/5.8 GHz 噪声干扰、GNSS 高精度欺骗、MAVLink 协议 DoS 攻击及信号重放，干扰成功率 ≥95%，系统成本仅为传统方案的 10%。
</div>

<div class="feature-card">
  <strong>🗄️ 双引擎数据仓库</strong><br>
  开发阶段采用 JSON 文件存储（易调试），生产环境无缝切换至 SQLite 关系型数据库（ACID 事务）。智能编码探测机制 100% 解决中文乱码问题，支持 HDF5 格式海量 IQ 数据归档。
</div>

---

## ⚙️ 技术原理

<div class="highlight-box" style="background:#f3f8ff;">
  <strong>形状化流程总览</strong><br>
  用不同图形表达职责：矩形=处理模块，圆角矩形=智能识别，菱形=决策判断，平行四边形=执行输出。
</div>

<div class="tech-flow">
  <div class="flow-node shape-rect">2.1 感知</div>
  <div class="flow-arrow">→</div>
  <div class="flow-node shape-round">2.2 指纹特征</div>
  <div class="flow-arrow">→</div>
  <div class="flow-node shape-round">2.3 智能分类</div>
  <div class="flow-arrow">→</div>
  <div class="flow-node shape-rect">2.4 定位跟踪</div>
  <div class="flow-arrow">→</div>
  <div class="flow-node shape-diamond"><span>2.5 对抗决策</span></div>
  <div class="flow-arrow">→</div>
  <div class="flow-node shape-parallelogram"><span>2.6 反馈闭环</span></div>
</div>

<div class="principle-grid">
  <div class="principle-card">
    <h4>▭ 2.1 信号感知与预处理</h4>
    <p>多节点 SDR 并行采样，GPS/PPS 同步。</p>
    <p>STFT + CFAR 完成时频分析与弱信号检测。</p>
  </div>
  <div class="principle-card">
    <h4>◉ 2.2 特征提取与射频指纹</h4>
    <p>小波包、MFCC、循环平稳特征联合建模。</p>
    <p>支持增量学习，快速适配新机型协议。</p>
  </div>
  <div class="principle-card">
    <h4>◉ 2.3 智能识别与分类</h4>
    <p>CNN 提取深度特征，SVM 提升小样本泛化。</p>
    <p>注意力 + 迁移学习，提高低信噪比识别率。</p>
  </div>
  <div class="principle-card">
    <h4>▭ 2.4 高精度定位与跟踪</h4>
    <p>TDOA 与 AOA 融合解算三维位置。</p>
    <p>EKF/IMM 持续跟踪并预测短时轨迹。</p>
  </div>
  <div class="principle-card">
    <h4>◇ 2.5 自适应干扰对抗</h4>
    <p>DQN 根据实时状态选择干扰策略。</p>
    <p>支持噪声压制、协议欺骗与链路阻断。</p>
  </div>
  <div class="principle-card">
    <h4>▱ 2.6 效能评估与闭环反馈</h4>
    <p>干扰后立即复测，判断是否失联/偏航。</p>
    <p>自动退避调参并沉淀日志用于策略迭代。</p>
  </div>
</div>

---
## 🏗️ 系统架构

### 3.1 总体架构分层

系统采用五层纵深防御架构，各层间通过标准化接口解耦，支持横向扩展与组件热插拔。

<div class="layer-stack">
  <div class="layer-row">扩展层 <em>REST / gRPC / SDK</em></div>
  <div class="layer-row">决策层 <em>规则引擎 / RL</em></div>
  <div class="layer-row">处理层 <em>GUI / 存储 / 加速</em></div>
  <div class="layer-row">传输层 <em>ZeroMQ / SSH</em></div>
  <div class="layer-row">感知层 <em>SDR / 视觉 / 雷达</em></div>
</div>

<p align="center">
  <img src="{{ '/图片1.png' | relative_url }}" alt="系统整体架构图" width="920">
</p>
<p align="center">图：系统整体架构</p>

### 3.2 感知层

- **SDR 传感器节点**：  
  - **主侦测设备**：RTL-SDR（低成本广域扫描）、HackRF One（半双工收发）、PlutoSDR（全双工教学级）。  
  - **部署方式**：支持 3–8 节点分布式组网，通过 GPS 授时模块（LEA-6T）实现纳秒级同步。  
  - **自动增益控制（AGC）**：自适应调整射频前端增益，防止强信号阻塞，动态范围 ≥ 80 dB。  
- **视觉传感器**：  
  - 工业级 IP 摄像机（H.265 编码，1080p@30fps），支持 RTSP/ONVIF 协议。  
  - 边缘端部署 Jetson AGX Orin，运行 YOLOv8s 模型（TensorRT 优化），检测帧率 ≥ 30 FPS。  
- **辅助传感器**：  
  - 气象站（风速、雨量），用于修正信号传播模型。  
  - 频谱监测仪（选配），校验 SDR 测量精度。  

### 3.3 传输层

- **低延迟消息总线**：基于 ZeroMQ 的 PUB/SUB 模式，节点间通信延迟 < 10 ms。所有 IQ 数据、特征向量及控制指令均以 Protobuf 格式序列化，压缩比 3:1。  
- **远程控制通道**：采用 Paramiko SSH 客户端与服务端架构，实现 HackRF 等设备的远程参数配置与数据流获取。支持 USB-over-IP 及 REST/ZeroRPC 两种代理模式，API 与本地 pyhackrf 100% 兼容。  
- **视频流传输**：通过 GStreamer 管道将 H.264 编码视频推送至 GUI 端，WebRTC 可选，延迟 ≤ 200 ms。  

### 3.4 处理层

- **图形用户界面**：  
  - 基于 PyQt6 构建，QML 编写部分动态组件，支持深色/浅色主题一键切换。  
  - 集成 Matplotlib（静态图表）与 PyQtGraph（实时频谱/瀑布图），渲染帧率 ≥ 25 FPS。  
  - 地图模块：使用 Leaflet.js 嵌入 QWebEngineView，实现 WGS84/GCJ02 坐标实时标绘。  
- **信号处理加速**：  
  - 计算密集型算法（FFT、FIR 滤波、相关运算）通过 Cython 编译为 C 扩展，或调用 Numba JIT 即时编译，性能提升 3–5 倍。  
  - 并行处理：利用 Python 多进程池，将不同频段扫描任务分配到多核 CPU。  
- **持久化存储**：  
  - **双引擎架构**：开发阶段使用 JSON 文件（human-readable），生产环境自动切换至 SQLite（事务支持）。  
  - **大数据存储**：原始 IQ 数据以 HDF5 格式压缩归档，单文件支持 TB 级存储，附带时间戳、中心频率等元数据。  

### 3.5 决策层

- **规则引擎**：基于 Rete 算法的轻量级规则库，预置 50+ 条威胁判定规则（如：信号强度 > -70 dBm 且持续 3 s → 可疑；位置接近禁飞区 → 威胁）。支持用户通过 GUI 动态增删规则。  
- **机器学习推理**：  
  - **本地推理**：TensorFlow Lite 模型（.tflite）大小 < 10 MB，在 CPU 上单次推理 < 15 ms。  
  - **硬件加速**：ONNX Runtime 调用 CUDA，在 Jetson 平台上模型推理时间 < 5 ms。  
- **策略管理**：  
  - 干扰策略通过 DQN 在线/离线训练生成，参数存储于 SQLite。  
  - 用户可自定义干扰波形（正弦波、扫频、噪声）及发射时序，通过 HackRF 任意波形生成接口下发。  

### 3.6 扩展层

- **API 接口**：  
  - RESTful API（Flask）：提供设备状态查询、历史威胁检索、干扰启停等操作，JSON 格式交互。  
  - gRPC 服务：用于高性能跨语言调用，支持 C++/Java/Go 客户端集成。  
- **Python SDK**：封装核心功能（频谱获取、识别、定位），提供 5 行代码快速接入示例，便于第三方开发者扩展。  
- **系统集成**：通过 Modbus TCP 与电子围栏系统联动；通过 Syslog 向安防中心转发告警事件。  

### 3.7 数据流说明

<div class="flow-board">
  <div class="flow-line">
    <div class="flow-box core">SDR 节点</div>
    <div class="flow-connector">→</div>
    <div class="flow-box">IQ 数据</div>
    <div class="flow-connector">→</div>
    <div class="flow-box core">传输层（ZeroMQ）</div>
    <div class="flow-connector">→</div>
    <div class="flow-box core">处理层</div>
  </div>
  <div class="flow-line offset-left">
    <div class="flow-box">特征提取</div>
    <div class="flow-connector">→</div>
    <div class="flow-box">识别模型</div>
    <div class="flow-connector">→</div>
    <div class="flow-box">定位解算</div>
    <div class="flow-connector">→</div>
    <div class="flow-box core">决策层</div>
  </div>
  <div class="flow-line offset-right">
    <div class="flow-box core">干扰策略</div>
    <div class="flow-connector">→</div>
    <div class="flow-box">发射指令</div>
    <div class="flow-connector">→</div>
    <div class="flow-box core">HackRF</div>
    <div class="flow-connector">→</div>
    <div class="flow-box">目标</div>
  </div>
  <div class="flow-line offset-left">
    <div class="flow-box">效能评估</div>
    <div class="flow-connector">←</div>
    <div class="flow-box">视觉反馈</div>
    <div class="flow-connector">←</div>
    <div class="flow-box">摄像头</div>
    <div class="flow-connector">←</div>
    <div class="flow-box">状态变化</div>
  </div>
</div>

---

## 📊 性能指标

| 指标项 | 实测值 | 备注 |
|--------|--------|------|
| **侦测频段** | 20 MHz – 6 GHz | 可扩展至 8 GHz（需更换前端） |
| **侦测灵敏度** | ≤ -100 dBm @ 2.4 GHz | 带宽 200 kHz |
| **最大侦测距离** | 3 km（视距） | 城市环境 0.5–1.5 km |
| **识别种类** | 32 种 | 含大疆、道通、派诺特、Skydio 等 |
| **识别准确率** | 94.7% | 高信噪比 ≥ 20 dB |
| **定位精度** | ≤ 3 m（二维），≤ 5 m（三维） | 4 节点组网，基线 ≥ 50 m |
| **响应时间** | 捕获 → 预警 ≤ 1.2 s，识别 → 干扰 ≤ 0.4 s | 含网络传输与决策延迟 |
| **干扰成功率** | 95% | 距离 500 m 内，主流消费级无人机 |
| **并发目标** | 单节点 12 个，多节点协同 ≥ 50 个 | 基于 ZeroMQ 负载均衡 |
| **系统可用性** | 99.95% | MTBF > 12,000 小时 |
| **误报率** | ≤ 2.1% | 标准电磁环境，无刻意干扰 |
| **页面加载性能** | 首次启动 26.7 s，后续平均 8.6 s | 瓶颈为 YOLO 模型加载，已优化为异步预加载 |
| **最大 IQ 记录速率** | 80 MB/s | HDF5 直接写入，无丢包 |

---

## 💻 软件与硬件

### 5.1 软件栈

| 类别 | 组件 | 作用 | 性能/特点 |
|------|------|------|-----------|
| **GUI 框架** | PyQt6 + QML | 主界面开发 | 跨平台，硬件加速渲染 |
| **实时绘图** | PyQtGraph | 频谱/瀑布图 | 60 FPS 渲染，百万点无卡顿 |
| **静态图表** | Matplotlib | 历史统计图 | 出版级矢量输出 |
| **数值计算** | NumPy, SciPy | 信号处理基础库 | BLAS/MKL 加速 |
| **时频分析** | PyWavelets | 小波包分解 | 瞬态特征提取 |
| **机器学习** | Scikit-learn, TensorFlow Lite, ONNX Runtime | 分类、决策、推理 | 模型压缩，边缘部署 |
| **数据库** | SQLite, JSON, HDF5 | 结构化数据、IQ 归档 | 双引擎切换，压缩存储 |
| **通信中间件** | ZeroMQ, Protobuf | 节点间通信 | 微秒级延迟，跨语言 |
| **远程控制** | Paramiko, gRPC | SSH 远程设备控制 | API 兼容 pyhackrf |
| **协议分析** | Scapy | WiFi/MAVLink 包构造 | 灵活、可编程 |
| **视频处理** | OpenCV, GStreamer | 视频流捕获与显示 | 硬件解码支持 |
| **Web 集成** | PyQt6.QWebEngineView | 内嵌地图、仪表盘 | JavaScript 双向通信 |
| **性能分析** | cProfile, py-spy | 热点定位 | 用于持续优化 |

### 5.2 硬件平台

| 设备类型 | 型号 | 数量（典型） | 技术规格 | 用途 |
|----------|------|--------------|----------|------|
| **SDR 主设备** | HackRF One | 1–4 | 1 MHz–6 GHz，20 MSPS，半双工 | 信号发射（干扰/欺骗）及接收 |
| **SDR 副设备** | RTL-SDR Blog V3 | 3–8 | 24 MHz–1.7 GHz，3.2 MSPS | 低成本广域频谱监测 |
| **全双工 SDR** | PlutoSDR / USRP B210 | 可选 | 70 MHz–6 GHz，56 MHz 带宽 | 高精度同步接收 |
| **边缘计算节点** | Jetson AGX Orin | 1–2 | 275 TOPS，32 GB 内存 | 视觉 AI 推理、局部信号处理 |
| **主控工作站** | 本地控制中心（定制） | 1 | 双 RTX 4090，64 GB RAM，NVMe RAID | 模型训练、多路信号分析、决策 |
| **远程控制终端** | 阿里云 01-KICKPI-K2B | ≥1 | 四核 A53，WiFi/以太网，预置远程服务 | HackRF 远程部署 |
| **天线系统** | 定向对数周期天线 | 2–4 | 700 MHz–6 GHz，增益 8–12 dBi | 信号接收与干扰发射 |
| **全向天线** | 宽带全向天线 | 2 | 2.4/5.8 GHz，增益 3–5 dBi | 广域侦测 |
| **GPS 授时模块** | Ublox LEA-6T / NEO-M8T | 3 | 10 ns 脉冲精度 | 多站 TDOA 同步 |
| **高稳晶振（OCXO）** | 0.1 ppm 恒温晶振 | 1 | 频率稳定度 0.1 ppb @ 1 s | GPS 欺骗必备，降低相位噪声 |
| **工业路由器** | 4G/5G CPE | 1 | 支持 VPN（WireGuard） | 边缘节点数据回传 |

---

## 📦 版本与信息

- **当前版本**：1.0.0（初始稳定版）  
- **发布日期**：2025 年 12 月  
- **开发团队**：Xuhui Li, Qixin Duan  
- **开源协议**：[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)  
- **兼容系统**：Ubuntu 20.04/22.04、Windows 10/11（WSL2）、CentOS 7+  
- **硬件依赖**：HackRF One / RTL-SDR（必需），NVIDIA GPU（推荐）  
- **路线图**：  
  - **v1.1**：5G NR-U 无人机检测与干扰  
  - **v1.2**：多站协作干扰波束赋形  
  - **v2.0**：全自动电子围栏联动，移动端监控 App  

<div class="highlight-box" style="background-color: #e7f5ff;">
  <p>🔮 <strong>未来愿景</strong>：构建城市级低空无人机态势感知与主动防御网络，让每一片天空都安全可控。</p>
</div>

---

*文档版本：1.0 · 最后更新：2026 年 2 月*
