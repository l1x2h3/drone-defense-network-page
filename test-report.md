---
title: Test Report
layout: home
nav_order: 3
permalink: /test-report/
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
  body,
  .main-content,
  .site-title,
  .site-nav,
  .search-input {
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
  .test-card {
    border: 1px solid rgba(148,163,184,.35);
    border-radius: 10px;
    padding: .9rem;
    margin: .8rem 0;
    background: rgba(255,255,255,.72);
  }
  .test-card h3 {
    margin-top: 0;
    color: #0b3d91;
    font-weight: 800;
    border-left: 4px solid rgba(59, 130, 246, .55);
    padding-left: .5rem;
  }
  .test-card p strong {
    color: #b45309;
  }
  .key-highlight {
    border: 1px solid rgba(96, 165, 250, .5);
    border-radius: 10px;
    background: rgba(219, 234, 254, .62);
    padding: .7rem .8rem;
    margin: .8rem 0 1rem;
    line-height: 1.7;
  }
  .key-highlight strong {
    color: #1d4ed8;
    font-weight: 800;
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
      max-width: 1080px !important;
      margin: 0 auto !important;
      padding: 1rem 1.5rem 2.4rem !important;
    }
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
  .image-row {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-bottom: 20px;
    gap: 1rem;
    width: 100%;
  }
  .image-row img {
    aspect-ratio: 4/3;
    height: auto;
    object-fit: contain;
    width: 100%;
    border-radius: 12px;
    border: 1px solid rgba(148, 163, 184, .32);
    box-shadow: 0 12px 26px rgba(15, 23, 42, .16);
    transition: transform .28s ease, box-shadow .28s ease;
    cursor: zoom-in;
  }
  .image-figure {
    margin: 0;
    text-align: center;
    width: 100%;
    border: 1px solid rgba(148, 163, 184, .26);
    border-radius: 14px;
    background: rgba(248, 250, 252, .5);
    padding: .65rem .65rem .5rem;
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    box-shadow: 0 10px 24px rgba(15, 23, 42, .10);
    animation: imgCardIn .45s ease both;
  }
  .image-figure:nth-child(2) {
    animation-delay: .08s;
  }
  .image-figure figcaption {
    margin-top: 8px;
    font-size: 14px;
    color: #333;
    font-weight: 500;
    line-height: 1.4;
  }
  .image-figure:hover img {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 16px 30px rgba(15, 23, 42, .2);
  }
  @keyframes imgCardIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  .img-lightbox {
    position: fixed;
    inset: 0;
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(2, 6, 23, .68);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    opacity: 0;
    pointer-events: none;
    transition: opacity .22s ease;
  }
  .img-lightbox.is-open {
    opacity: 1;
    pointer-events: auto;
  }
  .img-lightbox-content {
    position: relative;
    width: min(94vw, 1280px);
    max-height: 90vh;
    transform: scale(.96);
    transition: transform .22s ease;
  }
  .img-lightbox.is-open .img-lightbox-content {
    transform: scale(1);
  }
  .img-lightbox img {
    display: block;
    width: 100%;
    max-height: 90vh;
    object-fit: contain;
    border-radius: 14px;
    border: 1px solid rgba(148, 163, 184, .28);
    box-shadow: 0 20px 44px rgba(15, 23, 42, .45);
    background: rgba(15, 23, 42, .2);
  }
  .img-lightbox-close {
    position: absolute;
    top: -12px;
    right: -12px;
    width: 38px;
    height: 38px;
    border: 0;
    border-radius: 999px;
    color: #0f172a;
    font-size: 24px;
    line-height: 1;
    cursor: pointer;
    background: rgba(248, 250, 252, .95);
    box-shadow: 0 10px 24px rgba(15, 23, 42, .3);
  }
  caption, .fixed-caption {
    margin-top: 8px;
    font-size: 14px;
    color: #333;
    font-weight: 500;
    line-height: 1.4;
    text-align: center;
  }
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    text-align: center !important;
    vertical-align: middle;
  }
  table tbody tr:nth-child(odd) > td {
    background: rgba(239, 246, 255, .58) !important;
  }
  table tbody tr:nth-child(even) > td {
    background: rgba(241, 245, 249, .72) !important;
  }
  table thead tr {
    background: rgba(219, 234, 254, .86) !important;
  }
  .total-row td {
    background: rgba(191, 219, 254, 0.9) !important;
    font-weight: bold;
  }
  .average-col {
    background: rgba(219, 234, 254, 0.7) !important;
    font-weight: 500;
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
<script>
  document.addEventListener("DOMContentLoaded", function () {
    var targets = document.querySelectorAll(".image-row img");
    if (!targets.length) return;

    var overlay = document.createElement("div");
    overlay.className = "img-lightbox";
    overlay.setAttribute("aria-hidden", "true");
    overlay.innerHTML =
      '<div class="img-lightbox-content">' +
      '<button class="img-lightbox-close" type="button" aria-label="Close">&times;</button>' +
      '<img alt="preview">' +
      "</div>";

    document.body.appendChild(overlay);

    var preview = overlay.querySelector("img");
    var closeBtn = overlay.querySelector(".img-lightbox-close");

    function closeLightbox() {
      overlay.classList.remove("is-open");
      overlay.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
    }

    function openLightbox(src, alt) {
      preview.src = src;
      preview.alt = alt || "preview";
      overlay.classList.add("is-open");
      overlay.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
    }

    targets.forEach(function (img) {
      img.addEventListener("click", function () {
        openLightbox(img.currentSrc || img.src, img.alt);
      });
    });

    overlay.addEventListener("click", function (ev) {
      if (ev.target === overlay) closeLightbox();
    });

    closeBtn.addEventListener("click", closeLightbox);

    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && overlay.classList.contains("is-open")) {
        closeLightbox();
      }
    });
  });
</script>


## 无人机防御系统测试报告

<div class="key-highlight">
  <strong>报告用途：</strong>用于汇总各模块测试表现，快速识别瓶颈页面和关键风险点。<br>
  <strong>重点指标：</strong>识别准确率、页面加载时间、稳定运行时延与连续运行一致性。<br>
  <strong>建议关注：</strong>优先优化高耗时模块（如模型推理与统计页），并持续跟踪版本间性能回归。
</div>
<div class="test-card">
  <h3>1. 测试概述</h3>
  <p>&emsp;&emsp;我们基于已有的无人机防御软件系统开展了时间性能测试，记录了软件中各个页面（模块）的加载耗时，旨在提供系统性能的基准数据，并为进一步优化提供数据支撑。</p>
</div>
<div class="test-card">
  <h3>2. 测试环境、测试方法与性能指标</h3>
  <p>&emsp;&emsp;我们进行测试时的测试环境如表2-1所示，主要的性能指标要求如表2-2所示，测试方法为：使用添加了时间性能测试代码的main.py作为测试程序，通过代码中的时间记录功能精确测量每个页面的创建时间。连续运行程序10次，记录每次运行时各页面创建时间，并将其汇总到xlsx表格中。</p>
  <div style="display: flex; align-items: flex-start; gap: 20px;">
    <table>
      <caption>表2-1 测试环境</caption>
      <thead>
        <tr><th>名称</th><th>内容</th></tr>
      </thead>
      <tbody>
        <tr><td>硬件环境</td><td>4GB内存，2核处理器</td></tr>
        <tr><td>操作系统</td><td>Ubuntu 25.10 非LTS</td></tr>
        <tr><td>软件环境</td><td>Python3.12.9, PyQt6, Pytest</td></tr>
      </tbody>
    </table>
    <table>
      <caption>表2-2 主要性能指标</caption>
      <thead>
        <tr><th>性能指标</th><th>目标</th></tr>
      </thead>
      <tbody>
        <tr><td>平均加载用时</td><td><=15s</td></tr>
        <tr><td>最高加载用时</td><td><=30s</td></tr>
        <tr><td>稳定加载用时</td><td><=10s</td></tr>
      </tbody>
    </table>
  </div>
</div>
<div class="test-card">
  <h3>3. 测试结果与分析</h3>
  <p>&emsp;&emsp;通过进行测试，我们得到了如表3-1所示的表格。从表格中的测试数据可以看出，系统在第一次运行时加载时间最长，后续运行逐渐变短：首次运行总加载耗时26.69s，而到了第十次运行时总加载耗时8.61s，平均加载耗时11.62s。</p>
<div class="fixed-caption">表3-1 连续十次运行各页面加载耗时</div>
<table>
  <thead>
    <tr>
      <th>页面名称</th><th>第1次运行/s</th><th>第2次运行/s</th><th>第3次运行/s</th><th>第4次运行/s</th><th>第5次运行/s</th><th>第6次运行/s</th><th>第7次运行/s</th><th>第8次运行/s</th><th>第9次运行/s</th><th>第10次运行/s</th><th>平均加载各页面用时/s</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>主页</td><td>1.4019</td><td>0.2295</td><td>0.2117</td><td>0.2167</td><td>0.2276</td><td>0.22</td><td>0.2085</td><td>0.2158</td><td>0.2098</td><td>0.2153</td><td>0.33568</td></tr>
    <tr><td>设置页</td><td>0.0008</td><td>0.0009</td><td>0.0008</td><td>0.0008</td><td>0.0008</td><td>0.0008</td><td>0.0008</td><td>0.001</td><td>0.0007</td><td>0.0007</td><td>0.00081</td></tr>
    <tr><td>关于页</td><td>0.4937</td><td>0.4399</td><td>0.4544</td><td>0.4379</td><td>0.4659</td><td>0.4358</td><td>0.4421</td><td>0.4491</td><td>0.4367</td><td>0.4344</td><td>0.44899</td></tr>
    <tr><td>设备列表页</td><td>0.0086</td><td>0.0045</td><td>0.0046</td><td>0.0062</td><td>0.0052</td><td>0.0044</td><td>0.0044</td><td>0.0046</td><td>0.0045</td><td>0.0045</td><td>0.00515</td></tr>
    <tr><td>告警页</td><td>0.0315</td><td>0.0218</td><td>0.0224</td><td>0.0215</td><td>0.0226</td><td>0.026</td><td>0.0207</td><td>0.0239</td><td>0.0213</td><td>0.022</td><td>0.02337</td></tr>
    <tr><td>群组管理页</td><td>0.005</td><td>0.0026</td><td>0.0031</td><td>0.0025</td><td>0.0024</td><td>0.0026</td><td>0.0028</td><td>0.0033</td><td>0.0023</td><td>0.0025</td><td>0.00291</td></tr>
    <tr><td>入侵统计页</td><td>3.9642</td><td>5.2052</td><td>4.8284</td><td>3.7606</td><td>7.164</td><td>4.1074</td><td>4.4833</td><td>3.9383</td><td>3.5984</td><td>3.5543</td><td>4.46041</td></tr>
    <tr><td>发射页面</td><td>0.0144</td><td>0.0131</td><td>0.0113</td><td>0.0109</td><td>0.0107</td><td>0.0099</td><td>0.0099</td><td>0.0092</td><td>0.0106</td><td>0.0115</td><td>0.01115</td></tr>
    <tr><td>定位管理页</td><td>0.0635</td><td>0.0524</td><td>0.0471</td><td>0.0495</td><td>0.053</td><td>0.0479</td><td>0.0436</td><td>0.0474</td><td>0.0469</td><td>0.0468</td><td>0.04981</td></tr>
    <tr><td>Marvlink页</td><td>0.1762</td><td>0.0994</td><td>0.0688</td><td>0.0638</td><td>0.0893</td><td>0.0656</td><td>0.0616</td><td>0.0734</td><td>0.0765</td><td>0.0694</td><td>0.0844</td></tr>
    <tr><td>WiFi攻击页</td><td>0.0264</td><td>0.0256</td><td>0.0227</td><td>0.0199</td><td>0.0231</td><td>0.0175</td><td>0.0158</td><td>0.0173</td><td>0.0162</td><td>0.0206</td><td>0.02051</td></tr>
    <tr><td>GPS攻击页</td><td>0.0277</td><td>0.0214</td><td>0.0245</td><td>0.0201</td><td>0.0217</td><td>0.0149</td><td>0.012</td><td>0.0126</td><td>0.0181</td><td>0.0131</td><td>0.01861</td></tr>
    <tr><td>YOLO检测页</td><td>19.3653</td><td>4.6759</td><td>3.9861</td><td>4.6639</td><td>3.9291</td><td>4.0313</td><td>3.8941</td><td>4.2966</td><td>3.8886</td><td>3.8325</td><td>5.65634</td></tr>
    <tr><td>信号处理页</td><td>1.1082</td><td>0.5208</td><td>0.472</td><td>0.4988</td><td>0.4137</td><td>0.3923</td><td>0.3816</td><td>0.4295</td><td>0.4033</td><td>0.3873</td><td>0.50075</td></tr>
    <tr class="total-row"><td>总计</td><td>26.6874</td><td>11.313</td><td>10.1579</td><td>9.7731</td><td>12.4291</td><td>9.3764</td><td>9.5812</td><td>9.522</td><td>8.7339</td><td>8.6149</td><td>11.61889</td></tr>
  </tbody>
</table>
<p>&emsp;&emsp;根据表格中的数据，我们首先发现：<strong>系统加载时的性能瓶颈主要位于YOLO检测页与入侵统计页。</strong>连续10次运行后，YOLO检测页平均加载用时5.66s，入侵统计页平均加载用时4.46s，这两个页面的平均加载用时均远超信号处理页、关于页与主页等其它页面，如图3-1所示。而在图3-2所示的饼状图中也能够看到，加载YOLO检测页与入侵统计页这两个页面所用时间占比分别为48.68%与38.39%，均远超其它页面。</p>
<!-- 第一个图片行，包含两张并排显示的图片 -->
<div class="image-row">
  <figure class="image-figure">
    <!-- 显示平均页面加载时间的图片，src使用Liquid模板从站点的相对路径生成 -->
    <img id="average_page_load_time" src="{{ '/assets/images/average_page_load_time.png' | relative_url }}" alt="">
    <figcaption>图3-1 各页面平均加载用时</figcaption>
  </figure>
  <figure class="image-figure">
    <!-- 显示页面加载时间百分比的图片，同样使用Liquid模板生成路径 -->
    <img id="page_load_time_percentage" src="{{ '/assets/images/page_load_time_percentage.png' | relative_url }}" alt="">
    <figcaption>图3-2 各页面加载用时比例</figcaption>
  </figure>
</div>
<p>&emsp;&emsp;其次，<strong>系统初次加载耗时远高于后续加载耗时，尤其是YOLO检测页。</strong>系统初次运行时总加载用时高达26.69s，但是却在第二次运行时骤降至11.31s，之后不断走低，在第四次运行时加载用时低至9.77s。虽然在第五次运行时加载用时突增至12.43s，但是加载用时递减的趋势仍然持续，最终在第十次运行时加载用时8.61s，如图3-3所示。跟据图3-4，初次加载YOLO检测页时用时高达19.37s，随后骤降至4.68s，最终稳定在3.83s左右，而入侵统计页的加载用时则相对稳定在4s以下，仅在第五次运行时加载用时短暂升高至7.16s，因此由图3-4可知，虽然系统加载时的性能瓶颈主要位于YOLO检测页与入侵统计页，但是导致初次加载耗时远高于后续加载的并不是入侵统计页，而是YOLO检测页。</p>
<!-- 第二个图片行，包含另外两张并排显示的图片 -->
<div class="image-row">
  <figure class="image-figure">
    <!-- 显示每次运行总加载时间的图片，路径由Liquid模板生成 -->
    <img id="total_load_time_per_run" src="{{ '/assets/images/total_load_time_per_run (Edited).png' | relative_url }}" alt="">
    <figcaption>图3-3 总加载用时随运行次数变化趋势</figcaption>
  </figure>
  <figure class="image-figure">
    <!-- 显示每次运行YOLO入侵检测加载时间的图片，路径由Liquid模板生成 -->
    <img id="yolo_intrusion_load_time_per_run" src="{{ '/assets/images/yolo_intrusion_load_time_per_run (Edited).png' | relative_url }}" alt="">
    <figcaption>图3-4 YOLO检测页与入侵统计页加载用时变化趋势</figcaption>
  </figure>
</div>
<p>&emsp;&emsp;因此，本系统最高耗时26.69s，小于指标要求的30s；平均耗时11.62s，小于指标要求的15s；稳定加载用时约为8-9s，小于指标要求的10s，如表3-2所示。</p>
  <div class="fixed-caption">表3-2 性能指标要求与实际测量情况</div>
  <table>
    <thead>
      <tr><th>性能指标</th><th>目标</th><th>测量结果</th><th>状态</th></tr>
    </thead>
    <tbody>
      <tr><td>平均加载用时</td><td><=15s</td><td>11.62s</td><td><strong>通过</strong></td></tr>
      <tr><td>最高加载用时</td><td><=30s</td><td>26.69s</td><td><strong>通过</strong></td></tr>
      <tr><td>稳定加载用时</td><td><=10s</td><td><=10s</td><td><strong>通过</strong></td></tr>
    </tbody>
  </table>
</div>
<div class="test-card">
  <h3>4. 测试结论</h3>
  <p>&emsp;&emsp;<strong>通过。</strong>本测试报告记录了无人机防御系统在特定环境下的页面加载性能。系统在首次运行时加载时间最长，后续运行中加载时间逐渐减少。测试结果表明，YOLO检测页是系统启动时的主要性能瓶颈，平均加载时间达5.65634秒，首次运行高达19.3653秒。后续针对YOLO检测页初次耗时长的现象，预计将引入动态加载机制，仅在需要时才开启YOLO检测，借此来达到改善性能瓶颈的目的。</p>
</div>
