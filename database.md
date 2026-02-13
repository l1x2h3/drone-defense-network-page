---
title: Database
layout: home
nav_order: 2
permalink: /database/
---

<style>
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
  .db-table-wrap {
    overflow: auto;
    max-height: 70vh;
    border: 1px solid rgba(148,163,184,.35);
    border-radius: 10px;
    background: rgba(248,250,252,.68);
  }
  .db-table {
    width: 100%;
    min-width: 2200px;
    border-collapse: collapse;
    table-layout: fixed;
    font-size: .86rem;
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
  .header-quick-item a {
    color: inherit;
    text-decoration: none;
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



## Local Database Snapshot

<p class="db-note">Source: <code>drone_data.db</code> in repository root.</p>

### Table: drone_data

<p class="db-note">Rows: 10</p>
<div class="db-table-wrap">
<table class="db-table">
<colgroup><col style="width:70px"><col style="width:170px"><col style="width:260px"><col style="width:420px"><col style="width:480px"><col style="width:520px"><col style="width:180px"><col style="width:260px"></colgroup>
<thead><tr><th>id</th><th>name</th><th>communication_protocol</th><th>frequency_band</th><th>max_communication_distance</th><th>camera_resolution</th><th>video_bitrate</th><th>information_source</th></tr></thead>
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
