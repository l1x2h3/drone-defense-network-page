---
title: 数据库
layout: home
nav_order: 2
permalink: /database/
---

<style>
  :root {
    --font-body: "PingFang SC", "HarmonyOS Sans SC", "Microsoft YaHei", "Noto Sans SC", sans-serif;
    --font-heading: "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif;
  }
  body {
    background: #dbe3ee;
  }
  body::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: -2;
    background-image: url("{{ '/assets/images/background.jpg' | relative_url }}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: saturate(1.08) contrast(1.03);
  }
  body::after {
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;
    pointer-events: none;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    background: linear-gradient(180deg, rgba(241, 245, 249, .55), rgba(226, 232, 240, .45));
  }
  body, .main-content, .site-title, .site-nav, .search-input {
    font-family: var(--font-body) !important;
  }
  .site-header,
  .main-header {
    background: rgba(241, 245, 249, .28) !important;
    border-bottom: 1px solid rgba(148, 163, 184, .24) !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
  }
  .site-header {
    box-shadow: none !important;
  }
  .main-header .header-quick {
    background: rgba(248, 250, 252, .36);
    border: 1px solid rgba(148, 163, 184, .28);
    border-radius: 12px;
    padding: .35rem .6rem;
    box-shadow: 0 8px 24px rgba(15, 23, 42, .08);
  }
  .main-header .search,
  .main-header .search-input-wrap {
    background: rgba(248, 250, 252, .34) !important;
    border: 1px solid rgba(148, 163, 184, .28) !important;
    border-radius: 10px !important;
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    box-shadow: 0 8px 20px rgba(15, 23, 42, .08);
  }
  .main-header .search-input,
  .main-header .search-input:focus {
    background: transparent !important;
    border: 0 !important;
    box-shadow: none !important;
  }
  .main-header .search-input::placeholder {
    color: #64748b;
  }
  .header-quick-item {
    display: inline-flex;
    align-items: center;
    white-space: nowrap;
    font-size: .78rem;
    color: #475569;
    border: 1px solid rgba(148, 163, 184, .32);
    background: rgba(226, 232, 240, .3);
    border-radius: 999px;
    padding: .22rem .58rem;
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    transition: transform .22s ease,
                box-shadow .22s ease,
                border-color .22s ease,
                background-color .22s ease;
    transform-origin: center;
    will-change: transform;
  }
  @media (hover: hover) and (pointer: fine) {
    .header-quick-item:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 14px 30px rgba(15, 23, 42, .14);
        border-color: rgba(59, 130, 246, .35);
    }
  }
  @media (prefers-reduced-motion: reduce) {
    .header-quick-item {
        transition: none !important;
        transform: none !important;
    }
  }
  .product-nav {
    display: flex;
    flex-wrap: wrap;
    gap: .55rem;
    margin: .6rem 0 1rem;
  }
  .product-nav a {
    text-decoration: none;
    padding: .3rem .65rem;
    border: 1px solid rgba(148,163,184,.45);
    border-radius: 999px;
    background: rgba(226,232,240,.42);
    color: #334155;
    font-weight: 600;
    font-size: .9rem;
  }
  @media (min-width: 50rem) {
    .side-bar {
      display: none !important;
    }
    .main {
      margin-left: 0 !important;
      max-width: none !important;
    }
    .main-header,
    .main-content-wrap {
      max-width: none !important;
    }
    .main-content {
      max-width: none !important;
      width: auto !important;
      margin: 0 auto !important;
      padding: 1rem 1.5rem 2.2rem !important;
    }
  }

  .db-table-wrap {
    overflow: visible;
    width: 100%;
    border: 1px solid rgba(148,163,184,.35);
    border-radius: 12px;
    background: rgba(248,250,252,.72);
    box-shadow: 0 10px 26px rgba(15, 23, 42, .08);
  }
  .db-table {
    width: 100%;
    min-width: 0;
    border-collapse: collapse;
    table-layout: fixed;
    font-size: .84rem;
    line-height: 1.45;
  }
  .db-table th,
  .db-table td {
    border: 1px solid #dbe2ea;
    padding: .35rem .45rem;
    vertical-align: top;
    text-align: left;
    white-space: normal;
    word-break: break-word;
  }
  .db-table th {
    position: sticky;
    top: 0;
    z-index: 1;
    background: #dbeafe;
    font-weight: 700;
    text-transform: capitalize;
  }
  .db-table tbody tr:nth-child(odd) td {
    background: rgba(241, 245, 249, .55);
  }
  .db-table tbody tr:hover td {
    background: rgba(219, 234, 254, .45);
  }
  .db-table td:nth-child(4),
  .db-table td:nth-child(5),
  .db-table td:nth-child(6) {
    white-space: normal;
  }
  .db-table th:nth-child(1),
  .db-table th:nth-child(2),
  .db-table th:nth-child(3),
  .db-table td:nth-child(1),
  .db-table td:nth-child(2),
  .db-table td:nth-child(3) {
    text-align: center;
  }
  .db-note {
    color: #475569;
    font-size: .9rem;
    margin: .35rem 0 .9rem;
  }

  .header-quick {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: .45rem;
    flex: 1 1 auto;
    min-width: 0;
    padding: 0 .8rem;
  }
  .header-quick-item {
    display: inline-flex;
    align-items: center;
    white-space: nowrap;
    font-size: .78rem;
    color: #475569;
    border: 1px solid rgba(148, 163, 184, .32);
    background: rgba(226, 232, 240, .3);
    border-radius: 999px;
    padding: .22rem .58rem;
  }
  @media (max-width: 900px) {
    .header-quick { display: none; }
  }
</style>


<script>
  document.addEventListener("DOMContentLoaded", function () {
    var header = document.getElementById("main-header");
    if (!header || header.querySelector(".header-quick")) return;

    var quick = document.createElement("div");
    quick.className = "header-quick";
    quick.innerHTML =
      '<span class="header-quick-item"><a href="{{ '/' | relative_url }}">Page 1: Overview</a></span>' +
      '<span class="header-quick-item"><a href="{{ '/database/' | relative_url }}">Page 2: Database</a></span>' +
      '<span class="header-quick-item"><a href="{{ '/test-report/' | relative_url }}">Page 3: Test Report</a></span>' +
      '<span class="header-quick-item">Version: v1.0.0</span>' +
      '<span class="header-quick-item">System: Stable (sample)</span>';

    var aux = header.querySelector(".aux-nav");
    if (aux) {
      header.insertBefore(quick, aux);
    } else {
      header.appendChild(quick);
    }
  });
</script>



## 本地数据库快照

<p class="db-note">Source: <code>drone_data.db</code> in repository root.</p>

<div class="db-note" style="background: rgba(239, 246, 255, .72); border: 1px solid rgba(147, 197, 253, .45); border-radius: 10px; padding: .7rem .8rem; line-height: 1.7;">
  <strong>数据概括：</strong>本表汇总了系统可识别与可防御的无人机型号，覆盖消费级、行业级与特种任务机型。<br>
  <strong>类型范围：</strong>包含多旋翼航拍机、行业巡检机、安防侦察机以及长距通信机型，品牌覆盖 DJI、Autel、Yuneec、Hubsan、Skydio、Parrot 等。<br>
  <strong>防御意义：</strong>通过频段、协议、通信距离、视频链路和载荷能力等信息，可快速完成目标分类、干扰策略匹配和处置优先级判断。
</div>

### 数据表：drone_data

<p class="db-note">记录数：10</p>
<div class="db-table-wrap">
<table class="db-table">
<colgroup><col style="width:5%"><col style="width:8%"><col style="width:12%"><col style="width:20%"><col style="width:22%"><col style="width:23%"><col style="width:5%"><col style="width:5%"></colgroup>
<thead><tr><th>编号</th><th>型号</th><th>通信协议</th><th>频段</th><th>最大通信距离</th><th>相机分辨率</th><th>视频码率</th><th>信息来源</th></tr></thead>
<tbody>
<tr><td>1</td><td>DJI AIR 3S</td><td>O4、802.11 a/b/g/n/ac、蓝牙5.2</td><td>O4：2.4000 GHz 至 2.4835 GHz，5.170 GHz 至 5.250 GHz，5.725 GHz 至 5.850 GHz<br>802.11 a/b/g/n/ac：2.400 GHz 至 2.4835 GHz，5.725 GHz 至 5.850 GHz<br>蓝牙 5.2：2.400 GHz 至 2.4835 GHz</td><td>无干扰无遮挡：10 公里<br>强干扰：都市中心，约 1.5 至 4 公里<br>中干扰：近郊县城，约 4 至 10 公里<br>微干扰：远郊/海边，约 10 至 20 公里<br>微干扰有建筑物遮挡：约 0 公里至 0.5 公里<br>微干扰有树丛遮挡：约 0.5 公里至 3 公里</td><td>广角相机照片分辨率：8192×6144，5000万像素<br>广角相机视频分辨率：4K3840 × 2160/FHD1920 × 1080/竖拍 2.7K1512 × 2688<br>中长焦相机照片分辨率：8064×6048，4800万像素<br>中长焦相机视频分辨率：4K3840 × 2160/FHD1920 × 1080/竖拍 2.7K1512 × 2688</td><td>H.264/H.265 码率：130Mbps</td><td>https://www.dji.com/cn/air-3s/specs</td></tr>
<tr><td>2</td><td>DJI Mavic 4 Pro</td><td>O4+、802.11a/b/g/n/ac/ax、蓝牙 5.1</td><td>O4+：2.4000 GHz 至 2.4835 GHz，5.1700 GHz 至 5.2500 GHz，5.7250 GHz 至 5.8500 GHz<br>802.11a/b/g/n/ac/ax：2.4000 GHz 至 2.4835 GHz，5.7250 GHz 至 5.850 GHz<br>蓝牙 5.1：2.4000 GHz 至 2.4835 GHz</td><td>无干扰无遮挡：15 公里<br>强干扰（都市中心）：约 1.5 至 6 公里<br>中干扰（城郊县城）：约 6 至 15 公里<br>微干扰（远郊/海边）：约 15 至 30 公里<br>微干扰，有建筑物遮挡：约 0 至 0.7 公里<br>微干扰，有树丛遮挡：约 0.7 至 4.5 公里</td><td>哈苏相机照片分辨率：12288 × 8192，1亿像素<br>哈苏相机视频分辨率：6K6016×3384/DCI 4K4096×2160/4K3840×2160/FHD1920×1080/4K 竖拍2160×3840<br>中长焦相机照片分辨率： 8064 × 6048，4800万像素<br>中长焦相机视频分辨率：4K3840×2160/FHD1920×1080/2.7K 竖拍1512×2688<br>长焦相机照片分辨率：8192 × 6144，5000万像素<br>长焦相机视频分辨率：4K3840×2160/FHD1920×1080/2.7K 竖拍1512×2688</td><td>H.264 标准码率：90Mbps<br>H.265 标准码率：180Mbps<br>H.264 ALL-I 码率：1200Mbps</td><td>https://www.dji.com/cn/mavic-4-pro/specs</td></tr>
<tr><td>3</td><td>DJI Matrice 400</td><td>DJI O4 图传行业增强版、Wi-Fi Direct，Wireless Display，IEEE 802.11 a/b/g/n/ac/ax、蓝牙 5.2</td><td>DJI O4 图传行业增强版：902 MHz 至 928 MHz，2.400 GHz 至 2.4835 GHz，5.150 GHz 至 5.250 GHz，5.725 GHz 至 5.850 GHz<br>Wi-Fi Direct，Wireless Display，IEEE 802.11 a/b/g/n/ac/ax：2.4000 GHz 至 2.4835 GHz，5.150 GHz 至 5.250 GHz，5.725 GHz 至 5.850 GHz<br>蓝牙 5.2：2.400 GHz 至 2.4835 GHz</td><td>无干扰无遮挡：20 公里<br>强干扰（密集楼宇、居民区等）：约 1.5 至 6 公里<br>中干扰（城郊县城、城市公园等）：约 6 至 15 公里<br>弱干扰（远郊野外、开阔农田等）：约 15 至 40 公里</td><td>1080p</td><td>暂无</td><td>https://enterprise.dji.com/cn/matrice-400/specs</td></tr>
<tr><td>4</td><td>DJI Neo 2</td><td>标配 Wi-Fi 图传、可拓展 DJI Neo 2 数字图传模块（O4）、802.11a/b/g/n/ac/ax、蓝牙 5.2</td><td>标配 Wi-Fi 图传：2.400 GHz 至 2.4835 GHz，5.170 GHz 至 5.250 GHz，5.725 GHz 至 5.850 GHz<br>802.11a/b/g/n/ac/ax：2.400 GHz 至 2.4835 GHz，5.170 GHz 至 5.250 GHz，5.725 GHz 至 5.850 GHz<br>蓝牙 5.2：2.400 GHz 至 2.4835 GHz</td><td>无干扰无遮挡：6 公里<br>强干扰：都市中心，约 1.5 至 3 公里<br>中干扰：近郊县城，约 3 至 6 公里<br>微干扰：远郊/海边，约 6 至 10 公里<br>微干扰有建筑物遮挡：约 0 至 0.5 公里<br>微干扰有树丛遮挡：约 0.5 至 3 公里</td><td>照片分辨率：4000×3000（4:3）/4000×2250（16:9）1200 万像素<br>视频分辨率：横拍4K（4:3*）3840×2880/横拍1080p（4:3*）1440×1080/横拍4K（16:9）3840×2160/横拍1080p（16:9）1920×1080/竖拍2.7K（9:16）1512×2688</td><td>80Mbps</td><td>https://www.dji.com/cn/neo-2/specs</td></tr>
<tr><td>5</td><td>DJI Mini 5 Pro</td><td>O4+、802.11 a/b/g/n/ac/ax、蓝牙 5.4</td><td>O4+：2.400 GHz 至 2.4835 GHz，5.170 GHz 至 5.250 GHz，5.725 GHz 至 5.850 GHz<br>802.11 a/b/g/n/ac/ax：2.400 GHz 至 2.4835 GHz，5.725 GHz 至 5.850 GHz<br>蓝牙 5.4：2.400 GHz 至 2.4835 GHz</td><td>无干扰无遮挡：10 公里<br>强干扰：都市中心，约 1.5 公里至 4 公里<br>中干扰：近郊县城，约 4 公里至 10 公里<br>微干扰：远郊/海边，约 10 公里至 20 公里<br>微干扰有建筑物遮挡：约 0 公里至 0.7 公里<br>微干扰有树丛遮挡：约 0.7 公里至 4.5 公里</td><td>图片分辨率：8192×6144：5000万像素<br>视频分辨率：4K3840×2160/FHD：1920×1080</td><td>H.264/H.265 码率：130Mbps</td><td>https://www.dji.com/cn/mini-5-pro/specs</td></tr>
<tr><td>6</td><td>EVO II Pro V3</td><td>图传、802.11a/b/g/n/ac</td><td>图传：2.400-2.476GHz，2.400-2.4835GHz，5.725-5.829GHz，5.725-5.850GHz<br>802.11a/b/g/n/ac：2.400-2.476GHz，2.400-2.4835GHz，5.725-5.829GHz，5.725-5.850GHz</td><td>无干扰无遮挡8千米</td><td>图片分辨率：5472*3648 (3:2)/5472*3076 (16:9)/3840*2160 (16:9) 2000万像素<br>视频分辨率：5472×3076/3840×2160/2720×1528/1920×1080</td><td>120Mbps</td><td>https://www.autelrobotics.cn/productdetail/evo-ii-pro/#jsgg</td></tr>
<tr><td>7</td><td>TYPHOON H PLUS</td><td>WiFi</td><td>5.8GHz</td><td>最远1.6km</td><td>图片分辨率：4:3<br>视频分辨率：Full HD 1080p</td><td>暂无</td><td>https://www.yuneec.cn/product/showproduct.php?id=128</td></tr>
<tr><td>8</td><td>HUBSAN ACE 2+</td><td>SyncLeas 4+图传、4G、WiFi</td><td>暂无</td><td>最远14km</td><td>图片分辨率：8000*6048 4800万像素<br>视频分辨率：4K3840*2160/2.7K2720*1530/FHD1920*1080</td><td>100Mbps</td><td>https://chn.hubsan.com/index.php?main_page=product_info&amp;products_id=324</td></tr>
<tr><td>9</td><td>Skydio X10</td><td>WiFi6、蜂窝LTE/5G</td><td>WiFi6：2400-2483.5MHz，5150-5850MHz<br>蜂窝LTE/5G：600MHz-4400MHz</td><td>城市：1-2公里<br>郊区：2-6公里<br>农村：6-12公里<br>最大：12公里<br>5G：无限（无论有蜂窝网络覆盖）</td><td>长焦相机图片分辨率：8000 x 6000，4800万像素<br>长焦相机视频分辨率：3840 x 2880<br>广角相机图片分辨率：8192 x 6144，50.30百万像素<br>广角相机视频分辨率：3840 x 2880<br>窄摄像头图片分辨率：9248 x 6944，64MP<br>窄摄像头视频分辨率：3840 x 2880</td><td>暂无</td><td>https://www.skydio.com/x10/technical-specs</td></tr>
<tr><td>10</td><td>ANAFI-UKR</td><td>5G、Wi-Fi、MARS Radio、LoRa</td><td>暂无</td><td>5G：range without limits<br>Wi-Fi：5 km<br>MARS Radio：15 km<br>LoRa: 20 km</td><td>广角图片分辨率：21MP<br>直线型图片分辨率：16MP<br>视频分辨率：4K、FHD、HD</td><td>暂无</td><td>https://www.parrot.com/en/anafi-ukr-technical-specifications</td></tr>
</tbody></table>
</div>

### 无人机防御系统侦测产品对比

<p class="db-note">本表对比了主流无人机防御系统厂商的侦测类产品参数，包括侦测频段、距离、定位精度、多目标能力等关键指标。</p>
<div class="db-table-wrap">
<table class="db-table">
<colgroup><col style="width:12%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:16%"><col style="width:16%"></colgroup>
<thead><tr><th>对比项目</th><th>大公博创</th><th>海康威视</th><th>华御创新</th><th>历正科技</th><th>启垣防务</th><th>上海特金</th></tr></thead>
<tbody>
<tr><td>主要产品型号</td><td>DG-W1001/1002/1003/1004</td><td>D10RA/D02RP</td><td>A330/A340/A336/CHM-08</td><td>前哨系列/VAR系列/哨兵300</td><td>无</td><td>X1B/X1C/X1D Pro/H2L Pro</td></tr>
<tr><td>侦测频段</td><td>20MHz-8GHz (全频段)</td><td>26MHz-6GHz / 2.4G/5.8G</td><td>700MHz-6.3GHz</td><td>30MHz-6GHz</td><td>300MHz-6GHz</td><td>70MHz-6GHz</td></tr>
<tr><td>侦测距离</td><td>1-5km</td><td>1-10km (视环境)</td><td>1-7km</td><td>0-10km</td><td>5km</td><td>0.5-10km (视环境)</td></tr>
<tr><td>定位精度</td><td>≤10m (TDOA)</td><td>≤5° (测向)</td><td>支持定位</td><td>≤10m (TDOA)</td><td>无</td><td>≤10m (TDOA)</td></tr>
<tr><td>多目标能力</td><td>≥10架次</td><td>≤32架次</td><td>≥60架次</td><td>≥20架次</td><td>多目标</td><td>≥20架次</td></tr>
<tr><td>识别机型数量</td><td>大疆/道通等主流/穿越机/改频机</td><td>支持多频段无人机</td><td>≥35种</td><td>全机型库(1000+种)</td><td>支持主流无人机</td><td>700-1000+种</td></tr>
<tr><td>穿越机识别</td><td>支持</td><td>支持</td><td>A340专门支持FPV</td><td>支持</td><td>支持</td><td>支持</td></tr>
<tr><td>测向功能</td><td>支持 (≤3°精度)</td><td>支持 (≤5°精度)</td><td>支持</td><td>支持 (≤3°精度)</td><td>无</td><td>支持 (3°-10°精度)</td></tr>
<tr><td>防护等级</td><td>IP65</td><td>IP66/IP67</td><td>模块化设计</td><td>IP66</td><td>IP66</td><td>IP65/IP66</td></tr>
<tr><td>工作温度</td><td>-30℃~55℃</td><td>-20℃~60℃</td><td>-40℃~70℃</td><td>-40℃~70℃</td><td>未标注</td><td>-40℃~65℃</td></tr>
<tr><td>部署方式</td><td>固定式/手持式</td><td>固定式</td><td>模块化组件</td><td>固定式/移动式/手持式</td><td>固定式</td><td>固定式/手提式/手持式</td></tr>
</tbody></table>
</div>

### 无人机防御系统反制产品对比

<p class="db-note">本表对比了主流无人机防御系统厂商的反制类产品参数，包括反制频段、距离、方式、响应时间等关键指标。</p>
<div class="db-table-wrap">
<table class="db-table">
<colgroup><col style="width:12%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:16%"><col style="width:16%"></colgroup>
<thead><tr><th>对比项目</th><th>大公博创</th><th>海康威视</th><th>华御创新</th><th>历正科技</th><th>启垣防务</th><th>上海特金</th></tr></thead>
<tbody>
<tr><td>主要产品型号</td><td>DG-W2001/DG-W3001</td><td>五频段/六频段/D04JA</td><td>卫士三号/猎手三号</td><td>利剑P1/1000/3000</td><td>固定式/便携式干扰器</td><td>PX100/D2C-A2/H2D Pro</td></tr>
<tr><td>反制频段</td><td>1.2GHz-5.8GHz(4-7频段)</td><td>433M-5.8G(5-6频段)</td><td>300MHz-6GHz(多频段)</td><td>图传/数传/遥控(多频段)</td><td>840M-5.8G(多频段)</td><td>900M-5.8G(多频段)</td></tr>
<tr><td>反制距离</td><td>1-3km (围栏式)</td><td>干控比≤10:1</td><td>≥5km</td><td>0-3km</td><td>1.5-3km</td><td>0.5-2km</td></tr>
<tr><td>反制方式</td><td>定向频谱压制</td><td>多频段干扰</td><td>定向干扰多种模式</td><td>无线电压制式干扰</td><td>全向/定向干扰</td><td>宽频反制/精准反制</td></tr>
<tr><td>响应时间</td><td>≤4s</td><td>快速响应</td><td>≤5s</td><td>≤5s</td><td>快速响应</td><td>快速响应</td></tr>
<tr><td>多目标能力</td><td>多目标</td><td>多目标</td><td>≥8个目标</td><td>≥10-20架次</td><td>多目标</td><td>多目标</td></tr>
<tr><td>部署方式</td><td>固定式/车载</td><td>固定式/便携</td><td>固定式</td><td>固定式/便携/车载</td><td>固定式/便携</td><td>固定式/手持</td></tr>
<tr><td>防护等级</td><td>IP65</td><td>IP65</td><td>未标注</td><td>IP66</td><td>IP66</td><td>IP65</td></tr>
<tr><td>工作温度</td><td>-30℃~55℃</td><td>-20℃~55℃</td><td>-40℃~55℃</td><td>-40℃~65℃</td><td>未标注</td><td>-40℃~65℃</td></tr>
<tr><td>特殊功能</td><td>围栏式防护/组网联动</td><td>功率可调/电池续航</td><td>多干扰模式/7×24h工作</td><td>精准干扰/综合防御</td><td>自动防御/快速高效</td><td>察打一体/黑白名单</td></tr>
</tbody></table>
</div>

### 无人机防御系统诱骗产品对比

<p class="db-note">本表对比了主流无人机防御系统厂商的诱骗类产品参数，包括诱骗频段、范围、功率、效果等关键指标。</p>
<div class="db-table-wrap">
<table class="db-table">
<colgroup><col style="width:12%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:16%"><col style="width:16%"></colgroup>
<thead><tr><th>对比项目</th><th>大公博创</th><th>海康威视</th><th>华御创新</th><th>历正科技</th><th>启垣防务</th><th>上海特金</th></tr></thead>
<tbody>
<tr><td>主要产品型号</td><td>DG-W2002</td><td>无</td><td>无</td><td>天盾系列/潜盾系列/神枪手系列</td><td>无</td><td>ND10</td></tr>
<tr><td>诱骗频段</td><td>GPS/GLONASS</td><td>无</td><td>无</td><td>GPS-L1/GLONASS-L1(可扩展)</td><td>无</td><td>GPS L1/GLONASS L1</td></tr>
<tr><td>诱骗范围</td><td>0.5-1km</td><td>无</td><td>无</td><td>0-1km</td><td>无</td><td>≤500m (全向)</td></tr>
<tr><td>诱骗功率</td><td>10mW (可定制)</td><td>无</td><td>无</td><td>低功率</td><td>无</td><td>≤10mW (可调)</td></tr>
<tr><td>响应时间</td><td>≤10s</td><td>无</td><td>无</td><td>≤5s</td><td>无</td><td>＜3s</td></tr>
<tr><td>诱骗效果</td><td>迫降/航迹修正/禁飞管控</td><td>无</td><td>无</td><td>迫降/驱离(多模式)</td><td>无</td><td>定向驱离/拒止</td></tr>
<tr><td>部署方式</td><td>固定式</td><td>无</td><td>无</td><td>固定式/移动式/手持式</td><td>无</td><td>固定式</td></tr>
<tr><td>认证情况</td><td>无线电核准</td><td>无</td><td>无</td><td>国家无委核准</td><td>无</td><td>国家无委核准</td></tr>
<tr><td>特点</td><td>多制式卫星/穿越机有效</td><td>无</td><td>无</td><td>侦诱一体/多模诱骗</td><td>无</td><td>辐射功率小/无附带伤害</td></tr>
</tbody></table>
</div>

### 无人机防御系统综合能力对比

<p class="db-note">本表从产品线完整性、穿越机应对能力、组网协同能力、技术先进性等多个维度对比了主流无人机防御系统厂商的综合实力。</p>
<div class="db-table-wrap">
<table class="db-table">
<colgroup><col style="width:16%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:14%"></colgroup>
<thead><tr><th>评估维度</th><th>大公博创</th><th>海康威视</th><th>华御创新</th><th>历正科技</th><th>启垣防务</th><th>上海特金</th></tr></thead>
<tbody>
<tr><td>侦测产品线完整性</td><td>★★★★★(固定/手持/车载)</td><td>★★★☆☆(固定式为主)</td><td>★★★☆☆(模块化组件)</td><td>★★★★★(最全面)</td><td>★☆☆☆☆(无)</td><td>★★★★☆(多种形态)</td></tr>
<tr><td>反制产品线完整性</td><td>★★★★☆</td><td>★★★★☆</td><td>★★★☆☆</td><td>★★★★★</td><td>★★★☆☆</td><td>★★★★☆</td></tr>
<tr><td>诱骗产品能力</td><td>★★★★☆</td><td>★☆☆☆☆</td><td>★☆☆☆☆</td><td>★★★★★</td><td>★☆☆☆☆</td><td>★★★☆☆</td></tr>
<tr><td>穿越机应对能力</td><td>★★★★☆</td><td>★★★☆☆</td><td>★★★★★(A340专针对)</td><td>★★★★★</td><td>★★★☆☆</td><td>★★★★☆</td></tr>
<tr><td>组网协同能力</td><td>★★★★★(TDOA组网)</td><td>★★★★☆(平台管理)</td><td>★★★☆☆</td><td>★★★★★(多机组网)</td><td>★★☆☆☆</td><td>★★★★★(TDOA组网)</td></tr>
<tr><td>产品定价范围</td><td>8.8万-30万</td><td>6.6万-19.3万</td><td>模块化定价</td><td>3万-50万</td><td>固定式定价</td><td>3万-50万</td></tr>
<tr><td>适用场景丰富度</td><td>★★★★★</td><td>★★★☆☆</td><td>★★★☆☆</td><td>★★★★★</td><td>★★☆☆☆</td><td>★★★★★</td></tr>
<tr><td>技术先进性</td><td>★★★★☆</td><td>★★★☆☆</td><td>★★★★☆</td><td>★★★★★</td><td>★★☆☆☆</td><td>★★★★☆</td></tr>
</tbody></table>
</div>
