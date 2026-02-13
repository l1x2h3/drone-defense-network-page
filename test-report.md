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
</div>

<div class="test-card">
  <h3>4. Conclusion</h3>
  <p>Pass / Fail</p>
  <p>Open issues and priorities.</p>
</div>
