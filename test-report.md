---
title: Test Report
layout: home
nav_order: 3
permalink: /test-report/
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
  .test-card {
    border: 1px solid rgba(148,163,184,.35);
    border-radius: 10px;
    padding: .9rem;
    margin: .8rem 0;
    background: rgba(255,255,255,.72);
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



## Test Result Template

<div class="test-card">
  <h3>1. Test Overview</h3>
  <p>Test Date: YYYY-MM-DD</p>
  <p>Build Version: vX.Y.Z</p>
  <p>Environment: hardware/software setup</p>
</div>

<div class="test-card">
  <h3>2. Key Metrics</h3>
  <table>
    <thead>
      <tr><th>Metric</th><th>Target</th><th>Measured</th><th>Status</th></tr>
    </thead>
    <tbody>
      <tr><td>Recognition Accuracy</td><td>>= 95%</td><td>--</td><td>--</td></tr>
      <tr><td>Response Latency</td><td><= 1.5s</td><td>--</td><td>--</td></tr>
      <tr><td>System Availability</td><td>>= 99.9%</td><td>--</td><td>--</td></tr>
    </tbody>
  </table>
</div>

<div class="test-card">
  <h3>3. Evidence</h3>
  <p>Paste screenshots, logs, charts, and short observations here.</p>
  <p>- Screenshot A: ...</p>
  <p>- Screenshot B: ...</p>
  <p>- Log summary: ...</p>




<script>
(function() {
  function init() {
    // 获取四张图片元素
    const imageIds = [
      'average_page_load_time',
      'page_load_time_percentage',
      'total_load_time_per_run',
      'yolo_intrusion_load_time_per_run'
    ];
    const images = imageIds.map(id => document.getElementById(id)).filter(img => img !== null);
    if (images.length === 0) return;
    // 创建浮动坐标层
    const floatText = document.createElement('div');
    floatText.textContent = '';
    floatText.style.position = 'absolute';
    floatText.style.display = 'none';
    floatText.style.pointerEvents = 'none';
    floatText.style.zIndex = '9999';
    floatText.style.whiteSpace = 'nowrap';
    document.body.appendChild(floatText);
    // 更新浮层内容和位置
    function updateFloat(e) {
      const img = e.currentTarget;               // 当前悬浮的图片
      const rect = img.getBoundingClientRect();
      // 图片未加载完成时宽度为0，隐藏浮层
      if (rect.width === 0) {
        floatText.style.display = 'none';
        return;
      }
      // 计算相对于图片左上角的坐标
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;
      // 确保坐标在图片范围内（理论上总是成立，但做保护）
      if (mouseX >= 0 && mouseX <= rect.width && mouseY >= 0 && mouseY <= rect.height) {
        floatText.textContent = `(${Math.round(mouseX)}, ${Math.round(mouseY)})`;
        floatText.style.display = 'block';
        // 将浮层置于鼠标右下方10px处
        floatText.style.left = (e.pageX + 10) + 'px';
        floatText.style.top = (e.pageY + 10) + 'px';
      } else {
        floatText.style.display = 'none';
      }
    }
    function hideFloat() {
      floatText.style.display = 'none';
    }
    // 为每张图片绑定必要的事件
    images.forEach(img => {
      img.addEventListener('mouseenter', updateFloat);   // 鼠标进入时立即显示
      img.addEventListener('mousemove', updateFloat);    // 鼠标移动时更新
      img.addEventListener('mouseleave', hideFloat);     // 鼠标离开时隐藏
    });
  }
  // 等待 DOM 加载完成
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>
<!-- 定义一个CSS样式块，用于控制页面中图片行的布局和图片的显示方式 -->
<style>
  /* 设置图片行的flex容器样式：子元素水平均匀分布，垂直居中，底部边距20px，宽度100% */
  .image-row {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-bottom: 20px;
    width: 100%;
  }
  /* 设置图片行内所有img元素的统一样式：宽高比强制为4:3，高度自动，图片保持原始比例适应容器（可能留有空白） */
  .image-row img {
    aspect-ratio: 4/3;
    height: auto;
    object-fit: contain;
  }
  /* 为特定id的图片设置最大宽度，以控制其在页面上的显示大小 */
  #average_page_load_time {
    max-width: 47%;
  }
  #page_load_time_percentage {
    max-width: 43%;
  }
  #total_load_time_per_run {
    max-width: 45%;
  }
  #yolo_intrusion_load_time_per_run {
    max-width: 45%;
  }
</style>
<!-- 第一个图片行，包含两张并排显示的图片 -->
<div class="image-row">
  <!-- 显示平均页面加载时间的图片，src使用Liquid模板从站点的相对路径生成 -->
  <img id="average_page_load_time" src="{{ '/assets/images/average_page_load_time.png' | relative_url }}" alt="">
  <!-- 显示页面加载时间百分比的图片，同样使用Liquid模板生成路径 -->
  <img id="page_load_time_percentage" src="{{ '/assets/images/page_load_time_percentage.png' | relative_url }}" alt="">
</div>
<!-- 第二个图片行，包含另外两张并排显示的图片 -->
<div class="image-row">
  <!-- 显示每次运行总加载时间的图片，路径由Liquid模板生成 -->
  <img id="total_load_time_per_run" src="{{ '/assets/images/total_load_time_per_run.png' | relative_url }}" alt="">
  <!-- 显示每次运行YOLO入侵检测加载时间的图片，路径由Liquid模板生成 -->
  <img id="yolo_intrusion_load_time_per_run" src="{{ '/assets/images/yolo_intrusion_load_time_per_run.png' | relative_url }}" alt="">
</div>




<div class="test-card">
  <h3>4. Conclusion</h3>
  <p>Pass / Fail</p>
  <p>Open issues and priorities.</p>
</div>
