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
</style>

<div class="highlight-box">
  <p>🚀 <strong>系统概述</strong>：基于软件定义无线电（SDR）与人工智能深度融合的智能安防平台，采用“侦—识—定—扰—评”五维一体架构，实现从电磁感知到精准干扰的全链条闭环防护。</p>
</div>

## 🔧 核心功能

<div class="feature-card">
  <strong>模块化设计</strong><br>
  四大核心模块（监控中心、智能预警、设备管理、数据分析）支持热插拔与独立升级。
</div>

<div class="feature-card">
  <strong>可视化仪表盘</strong><br>
  集成地图视图、频谱热力图、威胁轨迹回放、设备拓扑图，支持多屏联动。
</div>

<div class="feature-card">
  <strong>多源数据融合</strong><br>
  覆盖20MHz–6GHz全频段，兼容Wi-Fi/蓝牙/GPS/4G/5G及主流遥控协议。
</div>

<div class="feature-card">
  <strong>实时频谱分析</strong><br>
  毫秒级刷新，支持瞬态信号捕获与跳频模式识别。
</div>

<div class="feature-card">
  <strong>协议逆向分析</strong><br>
  自动解析DJI OcuSync、Autel、Parrot等协议，支持指令解码与重放攻击识别。
</div>

<div class="feature-card">
  <strong>自适应干扰</strong><br>
  动态调整频率、带宽、功率及波束指向，实现“精准打击、最小附带”。
</div>

---

## ⚙️ 技术原理

<div class="section-header">信号检测层</div>
多通道IQ采样（最高20 MSPS）+ STFT/Wigner-Ville时频分析 + 多阈值CFAR弱信号检测。

<div class="section-header">特征提取层</div>
融合小波包分解、MFCC、循环平稳特征等构建RF指纹库，支持在线增量学习。

<div class="section-header">智能识别层</div>
CNN+SVM混合模型 + 注意力机制 + 迁移学习，小样本泛化能力强。

<div class="section-header">定位追踪层</div>
TDOA+AOA融合算法（≥3节点），亚米级三维定位 + 卡尔曼滤波轨迹预测。

<div class="section-header">干扰对抗层</div>
数字波束成形（DBF） + DQN动态优化干扰策略，支持GPS欺骗与遥控阻断双模。

<div class="section-header">效能评估层</div>
干扰后自动验证目标状态（失联/返航/坠毁），视觉辅助形成闭环反馈。

---

## 🏗️ 系统架构

| 层级 | 组件 |
|------|------|
| **感知层** | RTL-SDR/HackRF/PlutoSDR异构节点，GPS同步，AGC自动增益 |
| **传输层** | ZeroMQ低延迟消息总线（<10ms），Protobuf压缩传输 |
| **处理层** | PyQt6 GUI + Cython/Numba加速 + SQLite/JSON/HDF5持久化 |
| **决策层** | 规则引擎 + 机器学习模型 + 用户自定义策略动态加载 |
| **扩展层** | RESTful/gRPC API + Python SDK，无缝对接VMS/SOC平台 |

---

## 📊 性能指标

- **检测范围**：0.5–3 km（视距），城市0.3–1.5 km  
- **响应时间**：捕获→预警 < 1.5s，识别→干扰 < 0.5s  
- **识别种类**：30+ 主流型号（DJI/Autel/Parrot/Yuneec/Skydio）  
- **系统可用性**：99.95% MTBF > 10,000 小时  
- **误报率**：< 2.5%（标准干扰环境）  
- **并发能力**：单节点10+目标，多节点协同50+目标  

---

## 💻 软件与硬件

<div class="feature-card" style="border-left-color: #20c997;">
  <strong>前端框架</strong><br>
  PyQt6 + QML | Matplotlib静态图 | PyQtGraph实时渲染
</div>

<div class="feature-card" style="border-left-color: #fd7e14;">
  <strong>信号处理</strong><br>
  NumPy/SciPy | PyWavelets | scikit-signal | GNU Radio（可选）
</div>

<div class="feature-card" style="border-left-color: #6f42c1;">
  <strong>机器学习</strong><br>
  Scikit-learn | TensorFlow Lite（<10MB模型） | ONNX Runtime
</div>

<div class="feature-card" style="border-left-color: #dc3545;">
  <strong>硬件平台</strong><br>
  HackRF/BladeRF/USRP | Jetson AGX Orin边缘部署 | GPSDO纳秒同步
</div>

---

## 📦 版本信息

- **版本**：1.0.0（初始稳定版）  
- **作者**：Xuhui Li, Qixin Duan  
- **技术栈**：Python 3.8+, PyQt6, TensorFlow Lite, ZeroMQ, SQLite  
- **许可证**：[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)  
- **兼容系统**：Ubuntu 20.04/22.04, Windows 10/11 (WSL2), CentOS 7+  

<div class="highlight-box" style="background-color: #e7f5ff;">
  <p>🔮 <strong>未来路线图</strong>：视觉AI辅助识别 · 5G NR-U无人机检测 · 电子围栏联动 · 移动端监控App</p>
</div>