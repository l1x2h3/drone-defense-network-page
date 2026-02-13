---
title: SkySentinel Nexus无人机防御网络系统
layout: home
nav_order: 1
description: 基于SDR与AI的智能无人机防御平台
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
  h1, h2, h3, h4, h5, h6,
  .site-title,
  .nav-list .nav-list-item > .nav-list-link {
    font-family: var(--font-heading) !important;
    letter-spacing: .01em;
  }
  .feature-card {
    background: rgba(241, 245, 249, .34);
    border-left: 4px solid rgba(71, 85, 105, .45);
    padding: 1.2rem;
    margin: 1.5rem 0;
    border-radius: 0 4px 4px 0;
  }
  .feature-group-title {
    margin: 1.2rem 0 .6rem;
    font-weight: 700;
    color: #334155;
    border-left: 4px solid rgba(100, 116, 139, .56);
    padding-left: .55rem;
  }
  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: .75rem;
  }
  .feature-grid .feature-card {
    margin: 0;
    border-left-width: 3px;
    border-radius: 10px;
    background: rgba(248, 250, 252, .4);
    border: 1px solid rgba(148, 163, 184, .24);
    box-shadow: 0 6px 18px rgba(15, 23, 42, .035);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
  }
  .feature-grid .feature-card strong {
    display: inline-block;
    margin-bottom: .2rem;
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
    border: 1px solid rgba(148, 163, 184, .36);
    border-radius: 12px;
    padding: .85rem .9rem;
    background:
      radial-gradient(120% 120% at 0% 0%, rgba(255,255,255,.62), transparent 55%),
      rgba(255,255,255,.78);
    backdrop-filter: blur(4px);
    box-shadow: 0 8px 20px rgba(15, 23, 42, .06);
  }
  .principle-card:nth-child(1),
  .principle-card:nth-child(4) { background-color: rgba(219, 234, 254, .5); border-color: rgba(96, 165, 250, .45); }
  .principle-card:nth-child(2),
  .principle-card:nth-child(3) { background-color: rgba(209, 250, 229, .45); border-color: rgba(16, 185, 129, .38); }
  .principle-card:nth-child(5),
  .principle-card:nth-child(6) { background-color: rgba(254, 243, 199, .5); border-color: rgba(245, 158, 11, .42); }
  .principle-card h4 {
    margin: 0 0 .45rem;
    font-size: 1.14rem;
    font-weight: 700;
    line-height: 1.3;
    color: #0b3d91;
  }
  .principle-card p {
    margin: .25rem 0;
    font-size: .88rem;
    line-height: 1.6;
    color: #4b5563;
  }
  .layer-stack {
    max-width: 860px;
    margin: 1rem auto 1.4rem;
    border: 1px solid rgba(148, 163, 184, .35);
    border-radius: 14px;
    overflow: hidden;
    background:
      radial-gradient(120% 100% at 10% 0%, rgba(56, 189, 248, .14), transparent 55%),
      radial-gradient(120% 100% at 100% 100%, rgba(96, 165, 250, .18), transparent 50%),
      rgba(255, 255, 255, .78);
    backdrop-filter: blur(6px);
    box-shadow: 0 14px 30px rgba(15, 23, 42, .08);
  }
  .layer-row {
    padding: .75rem 1rem;
    text-align: center;
    font-weight: 600;
    border-top: 1px solid rgba(203, 213, 225, .42);
    background: linear-gradient(180deg, rgba(255,255,255,.82) 0%, rgba(248,250,252,.68) 100%);
  }
  .layer-row:first-child {
    border-top: 0;
  }
  .layer-row:nth-child(1) { background: linear-gradient(180deg, rgba(219, 234, 254, .72), rgba(191, 219, 254, .35)); }
  .layer-row:nth-child(2) { background: linear-gradient(180deg, rgba(224, 242, 254, .72), rgba(186, 230, 253, .35)); }
  .layer-row:nth-child(3) { background: linear-gradient(180deg, rgba(236, 253, 245, .72), rgba(167, 243, 208, .34)); }
  .layer-row:nth-child(4) { background: linear-gradient(180deg, rgba(254, 249, 195, .72), rgba(253, 224, 71, .3)); }
  .layer-row:nth-child(5) { background: linear-gradient(180deg, rgba(254, 226, 226, .72), rgba(252, 165, 165, .3)); }
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
    background: rgba(255, 255, 255, .78);
    border: 1px solid rgba(148, 163, 184, .34);
    border-radius: 10px;
    padding: .45rem .7rem;
    font-size: .92rem;
    font-weight: 600;
    color: #1f2937;
    backdrop-filter: blur(4px);
    box-shadow: 0 6px 18px rgba(15, 23, 42, .06);
  }
  .flow-box.core {
    background: linear-gradient(180deg, rgba(191, 219, 254, .72), rgba(147, 197, 253, .45));
    border-color: rgba(96, 165, 250, .52);
    color: #0b3d91;
  }
  .flow-line:nth-child(2) .flow-box { background: linear-gradient(180deg, rgba(220, 252, 231, .72), rgba(187, 247, 208, .42)); border-color: rgba(74, 222, 128, .4); }
  .flow-line:nth-child(3) .flow-box { background: linear-gradient(180deg, rgba(254, 240, 138, .72), rgba(253, 224, 71, .34)); border-color: rgba(250, 204, 21, .45); }
  .flow-line:nth-child(4) .flow-box { background: linear-gradient(180deg, rgba(254, 226, 226, .72), rgba(252, 165, 165, .34)); border-color: rgba(248, 113, 113, .42); }
  .flow-connector {
    color: rgba(71, 85, 105, .85);
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
  .arch-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: .8rem;
    margin: .8rem 0 1.4rem;
  }
  .arch-card {
    background:
      radial-gradient(120% 120% at 0% 0%, rgba(255,255,255,.55), transparent 50%),
      rgba(255, 255, 255, .74);
    border: 1px solid rgba(148, 163, 184, .35);
    border-radius: 12px;
    padding: .8rem .9rem;
    backdrop-filter: blur(6px);
    box-shadow: 0 10px 24px rgba(15, 23, 42, .06);
  }
  .arch-card:nth-child(3n+1) { border-color: rgba(59, 130, 246, .45); background-color: rgba(219, 234, 254, .45); }
  .arch-card:nth-child(3n+2) { border-color: rgba(16, 185, 129, .4); background-color: rgba(209, 250, 229, .42); }
  .arch-card:nth-child(3n) { border-color: rgba(245, 158, 11, .45); background-color: rgba(254, 243, 199, .45); }
  .arch-card h4 {
    margin: 0 0 .45rem;
    font-size: 1.12rem;
    font-weight: 700;
    line-height: 1.3;
    color: #0b3d91;
  }
  .arch-card p {
    margin: .2rem 0;
    font-size: .88rem;
    line-height: 1.6;
    color: #4b5563;
  }
  .arch-top-nav {
    display: flex;
    flex-wrap: wrap;
    gap: .5rem;
    margin: .8rem 0 1rem;
    padding: .7rem;
    border: 1px solid rgba(148, 163, 184, .26);
    border-radius: 12px;
    background: rgba(241, 245, 249, .28);
    backdrop-filter: blur(4px);
  }
  .arch-top-nav a {
    text-decoration: none;
    color: #334155;
    font-weight: 600;
    font-size: .9rem;
    padding: .35rem .6rem;
    border: 1px solid rgba(148, 163, 184, .38);
    border-radius: 999px;
    background: rgba(226, 232, 240, .32);
  }
  .arch-shell {
    display: block;
  }
  .arch-sidebar {
    position: static;
    border: 1px solid rgba(148, 163, 184, .35);
    border-radius: 12px;
    padding: .7rem;
    background: rgba(255, 255, 255, .72);
    backdrop-filter: blur(4px);
    margin: 0 0 1rem;
  }
  .arch-sidebar h4 {
    margin: 0 0 .45rem;
    font-size: .95rem;
    color: #0b3d91;
  }
  .arch-sidebar-links {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: .2rem .4rem;
  }
  .arch-sidebar a {
    display: block;
    text-decoration: none;
    color: #334155;
    padding: .3rem .35rem;
    border-radius: 6px;
    font-size: .9rem;
  }
  .arch-sidebar a:hover {
    background: rgba(219, 234, 254, .8);
    color: #0b3d91;
  }
  .arch-main {
    min-width: 0;
  }
  .product-nav {
    display: flex;
    flex-wrap: wrap;
    gap: .55rem;
    margin: .9rem 0 1rem;
    padding: .65rem;
    border: 1px solid rgba(148, 163, 184, .24);
    border-radius: 12px;
    background: rgba(241, 245, 249, .24);
    backdrop-filter: blur(6px);
  }
  .product-nav a {
    text-decoration: none;
    color: #334155;
    font-weight: 600;
    font-size: .88rem;
    padding: .34rem .62rem;
    border-radius: 999px;
    border: 1px solid rgba(148, 163, 184, .34);
    background: rgba(226, 232, 240, .3);
  }
  .product-nav a:hover {
    background: rgba(203, 213, 225, .42);
  }
  .top-info-bar {
    display: flex;
    flex-wrap: wrap;
    gap: .5rem;
    margin: .15rem 0 1rem;
  }
  .top-info-chip {
    display: inline-flex;
    align-items: center;
    padding: .28rem .62rem;
    border-radius: 999px;
    font-size: .8rem;
    color: #475569;
    border: 1px solid rgba(148, 163, 184, .32);
    background: rgba(226, 232, 240, .24);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
  }
  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: .75rem;
    margin: .85rem 0 1.1rem;
  }
  .kpi-card {
    border: 1px solid rgba(148, 163, 184, .32);
    border-radius: 14px;
    padding: .72rem .8rem;
    background:
      radial-gradient(120% 120% at 0% 0%, rgba(255,255,255,.62), transparent 55%),
      rgba(255, 255, 255, .78);
    box-shadow: 0 8px 22px rgba(15, 23, 42, .06);
  }
  .kpi-card:nth-child(1) { border-color: rgba(59, 130, 246, .42); background-color: rgba(219, 234, 254, .45); }
  .kpi-card:nth-child(2) { border-color: rgba(16, 185, 129, .4); background-color: rgba(209, 250, 229, .43); }
  .kpi-card:nth-child(3) { border-color: rgba(245, 158, 11, .45); background-color: rgba(254, 243, 199, .44); }
  .kpi-card:nth-child(4) { border-color: rgba(168, 85, 247, .38); background-color: rgba(243, 232, 255, .5); }
  .kpi-label {
    font-size: .78rem;
    color: #64748b;
    margin-bottom: .28rem;
  }
  .kpi-value {
    font-size: 1.28rem;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.2;
  }
  .kpi-note {
    margin-top: .22rem;
    font-size: .8rem;
    color: #475569;
  }
  .ui-showcase {
    margin: 1.1rem 0 1.3rem;
    border: 1px solid rgba(148, 163, 184, .34);
    border-radius: 18px;
    padding: 1rem;
    background:
      radial-gradient(120% 140% at 0% 0%, rgba(255,255,255,.56), transparent 50%),
      rgba(255, 255, 255, .46);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    box-shadow: 0 18px 40px rgba(15, 23, 42, .12);
  }
  .ui-showcase h3 {
    margin: 0 0 .7rem;
    font-size: 1.08rem;
    color: #0b3d91;
  }
  .ui-frame {
    border-radius: 14px;
    padding: .6rem;
    background:
      linear-gradient(135deg, rgba(59, 130, 246, .32), rgba(16, 185, 129, .26)),
      rgba(15, 23, 42, .18);
    box-shadow:
      0 10px 24px rgba(15, 23, 42, .16),
      inset 0 1px 0 rgba(255, 255, 255, .4);
  }
  .ui-frame img {
    display: block;
    width: 100%;
    height: auto;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, .55);
    box-shadow: 0 8px 20px rgba(15, 23, 42, .24);
  }
  .ui-note {
    margin: .55rem 0 0;
    font-size: .84rem;
    color: #475569;
    text-align: center;
  }
  .ui-gallery {
    margin-top: .95rem;
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: .8rem;
  }
  .ui-gallery-card {
    border: 1px solid rgba(148, 163, 184, .34);
    border-radius: 12px;
    padding: .55rem;
    background: rgba(255, 255, 255, .72);
    box-shadow: 0 8px 20px rgba(15, 23, 42, .08);
  }
  .ui-gallery-title {
    font-size: .86rem;
    font-weight: 700;
    color: #334155;
    margin: 0 0 .45rem;
    text-align: center;
  }
  .ui-gallery-frame {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid rgba(226, 232, 240, .85);
    background: rgba(241, 245, 249, .68);
  }
  .ui-gallery-frame img {
    display: block;
    width: 100%;
    height: auto;
  }
  .ui-frame img,
  .ui-gallery-frame img {
    cursor: zoom-in;
  }
  .img-lightbox {
    position: fixed;
    inset: 0;
    z-index: 1200;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2.2rem 1rem;
    background: rgba(2, 6, 23, .72);
    opacity: 0;
    visibility: hidden;
    transition: opacity .24s ease, visibility .24s ease;
  }
  .img-lightbox.is-open {
    opacity: 1;
    visibility: visible;
  }
  .img-lightbox-content {
    position: relative;
    width: min(1100px, 92vw);
    max-height: 88vh;
    transform: scale(.94);
    opacity: 0;
    transition: transform .26s ease, opacity .26s ease;
  }
  .img-lightbox.is-open .img-lightbox-content {
    transform: scale(1);
    opacity: 1;
  }
  .img-lightbox img {
    display: block;
    width: 100%;
    height: auto;
    max-height: 88vh;
    object-fit: contain;
    border-radius: 12px;
    border: 1px solid rgba(148, 163, 184, .36);
    box-shadow: 0 24px 70px rgba(2, 6, 23, .45);
    background: rgba(15, 23, 42, .45);
  }
  .img-lightbox-close {
    position: absolute;
    top: -12px;
    right: -12px;
    width: 36px;
    height: 36px;
    border: 0;
    border-radius: 999px;
    background: rgba(15, 23, 42, .82);
    color: #f8fafc;
    font-size: 1.35rem;
    line-height: 1;
    cursor: pointer;
    box-shadow: 0 8px 20px rgba(2, 6, 23, .35);
  }
  @media (max-width: 900px) {
    .arch-sidebar {
      position: static;
    }
    .arch-sidebar-links {
      grid-template-columns: 1fr;
    }
    .kpi-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
    .ui-gallery {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
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
    .main-content-wrap {
      max-width: none !important;
      display: block !important;
    }
    .main-content {
      max-width: 1180px !important;
      width: auto !important;
      margin: 0 auto !important;
      padding: 1.1rem 2rem 3rem !important;
    }
  }
  .page-toc-floating {
    position: fixed;
    right: 20px;
    top: 92px;
    left: auto;
    width: 220px;
    max-height: calc(100vh - 120px);
    overflow: auto;
    z-index: 8;
    border: 1px solid rgba(148, 163, 184, .28);
    border-radius: 12px;
    background: rgba(226, 232, 240, .28);
    backdrop-filter: blur(6px);
    box-shadow: 0 10px 24px rgba(15, 23, 42, .08);
    padding: .65rem;
  }
  .page-toc-floating h4 {
    margin: 0 0 .45rem;
    font-size: .92rem;
    color: #334155;
  }
  .page-toc-floating a {
    display: block;
    text-decoration: none;
    color: #475569;
    padding: .26rem .35rem;
    border-radius: 6px;
    font-size: .86rem;
  }
  .page-toc-floating a.sub {
    padding-left: .95rem;
    color: #64748b;
    font-size: .82rem;
  }
  .page-toc-floating a:hover {
    background: rgba(148, 163, 184, .24);
    color: #1e293b;
  }
  .main-header {
    background: rgba(226, 232, 240, .26) !important;
    border-bottom: 1px solid rgba(148, 163, 184, .24) !important;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
  }
  .main-header .search {
    flex: 0 1 360px;
    max-width: 360px;
  }
  .main-header .aux-nav {
    margin-left: auto;
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
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
  }
  .search-input,
  .search-input:focus {
    background: rgba(248, 250, 252, .42) !important;
    border-color: rgba(148, 163, 184, .3) !important;
  }
  .aux-nav .site-button {
    background: rgba(226, 232, 240, .34) !important;
    border: 1px solid rgba(148, 163, 184, .3) !important;
    color: #334155 !important;
  }
  .aux-nav .site-button:hover {
    background: rgba(203, 213, 225, .42) !important;
    color: #1e293b !important;
  }
  .arch-sidebar {
    border-color: rgba(148, 163, 184, .28);
    background: rgba(226, 232, 240, .24);
  }
  .arch-sidebar h4 {
    color: #334155;
  }
  .arch-sidebar a {
    color: #475569;
  }
  .arch-sidebar a:hover {
    background: rgba(148, 163, 184, .24);
    color: #1e293b;
  }
  .table-wrapper table,
  table {
    width: 100%;
    border-collapse: collapse;
  }
  .table-wrapper table th,
  .table-wrapper table td,
  table th,
  table td {
    text-align: center !important;
    vertical-align: middle;
  }
  .table-wrapper table tbody tr:nth-child(odd) > td,
  table tbody tr:nth-child(odd) > td {
    background: rgba(239, 246, 255, .58) !important;
  }
  .table-wrapper table tbody tr:nth-child(even) > td,
  table tbody tr:nth-child(even) > td {
    background: rgba(241, 245, 249, .72) !important;
  }
  .table-wrapper table thead tr,
  table thead tr {
    background: rgba(219, 234, 254, .86) !important;
  }
  .feature-grid .feature-card,
  .principle-card,
  .arch-card,
  .kpi-card,
  .ui-showcase,
  .flow-box,
  .top-info-chip,
  .header-quick-item {
    transition:
      transform .22s ease,
      box-shadow .22s ease,
      border-color .22s ease,
      background-color .22s ease;
    transform-origin: center;
    will-change: transform;
  }
  @media (hover: hover) and (pointer: fine) {
    .feature-grid .feature-card:hover,
    .principle-card:hover,
    .arch-card:hover,
    .kpi-card:hover,
    .ui-showcase:hover,
    .flow-box:hover,
    .top-info-chip:hover,
    .header-quick-item:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 14px 30px rgba(15, 23, 42, .14);
      border-color: rgba(59, 130, 246, .35);
    }
  }
  @media (prefers-reduced-motion: reduce) {
    .feature-grid .feature-card,
    .principle-card,
    .arch-card,
    .kpi-card,
    .ui-showcase,
    .flow-box,
    .top-info-chip,
    .header-quick-item {
      transition: none !important;
      transform: none !important;
    }
  }
  @media (max-width: 1400px) {
    .page-toc-floating {
      display: none;
    }
  }
  @media (max-width: 900px) {
    .header-quick {
      display: none;
    }
    .main-header .search {
      flex: 1 1 auto;
      max-width: none;
    }
  }
  @media (max-width: 560px) {
    .ui-gallery {
      grid-template-columns: 1fr;
    }
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
    var targets = document.querySelectorAll(".ui-frame img, .ui-gallery-frame img");
    if (!targets.length) return;

    var overlay = document.createElement("div");
    overlay.className = "img-lightbox";
    overlay.setAttribute("aria-hidden", "true");
    overlay.innerHTML =
      '<div class="img-lightbox-content">' +
      '<button class="img-lightbox-close" type="button" aria-label="Close">&times;</button>' +
      '<img alt="preview">' +
      '</div>';

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


<div class="page-toc-floating">
  <h4>全文目录</h4>
  <a href="#sec-overview">系统概述</a>
  <a href="#sec-ui">界面展示</a>
  <a href="#sec-core">核心功能</a>
  <a href="#sec-tech">技术原理</a>
  <a href="#sec-arch">系统架构</a>
  <a class="sub" href="#arch-31">3.1 总体架构分层</a>
  <a class="sub" href="#arch-32">3.2 感知层</a>
  <a class="sub" href="#arch-33">3.3 传输层</a>
  <a class="sub" href="#arch-34">3.4 处理层</a>
  <a class="sub" href="#arch-35">3.5 决策层</a>
  <a class="sub" href="#arch-36">3.6 扩展层</a>
  <a class="sub" href="#arch-37">3.7 数据流说明</a>
  <a href="#sec-metrics">性能指标</a>
  <a href="#sec-stack">软件与硬件</a>
  <a href="#sec-meta">版本与信息</a>
</div>

<div id="sec-overview"></div>
# SkySentinel Nexus 无人机防御网络系统  
**基于SDR与AI的智能电磁感知与精准反制平台**  

<div class="top-info-bar">
  <span class="top-info-chip">部署形态：本地 / 边缘 / 云端（样例）</span>
  <span class="top-info-chip">更新频率：每月迭代（样例）</span>
  <span class="top-info-chip">服务支持：7×24 技术支持（样例）</span>
  <span class="top-info-chip">交付方式：源码 + 文档 + 培训（样例）</span>
</div>

<div class="kpi-grid">
  <div class="kpi-card">
    <div class="kpi-label">识别准确率</div>
    <div class="kpi-value">94.7%</div>
    <div class="kpi-note">高信噪比 ≥ 20 dB</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">定位精度</div>
    <div class="kpi-value">≤ 3 m</div>
    <div class="kpi-note">二维定位（4 节点）</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">干扰成功率</div>
    <div class="kpi-value">95%</div>
    <div class="kpi-note">500 m 内主流机型</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">系统可用性</div>
    <div class="kpi-value">99.95%</div>
    <div class="kpi-note">MTBF &gt; 12,000 小时</div>
  </div>
</div>

<div class="highlight-box">
  <p>🚀 <strong>系统概述</strong>：本系统是业界首套将软件定义无线电（SDR）、深度学习、高精度定位与自适应干扰技术深度融合的智能安防平台。采用“侦—识—定—扰—评”五维闭环架构，从电磁频谱感知到多手段协同反制，实现全天候、全频段、全协议的低空无人机防御，关键技术指标达到国际先进水平。</p>
</div>

<div id="sec-ui"></div>
## 🖥️ 界面展示

<div class="ui-showcase">
  <h3>&#20027;&#25511;&#24179;&#21488;&#30028;&#38754;</h3>
  <div class="ui-frame">
    <img src="{{ '/assets/images/main_page.png' | relative_url }}" alt="&#26080;&#20154;&#26426;&#38450;&#24481;&#32593;&#32476;&#31995;&#32479;&#20027;&#30028;&#38754;">
  </div>
  <p class="ui-note">&#31995;&#32479;&#20027;&#30028;&#38754;&#23637;&#31034;&#65288;&#23454;&#26102;&#39057;&#35889;&#12289;&#24577;&#21183;&#20449;&#24687;&#19982;&#25511;&#21046;&#38754;&#26495;&#65289;</p>

  <div class="ui-gallery">
    <div class="ui-gallery-card">
      <div class="ui-gallery-title">GPS &#25915;&#20987;&#30028;&#38754;</div>
      <div class="ui-gallery-frame">
        <img src="{{ '/assets/images/gps_attack.png' | relative_url }}" alt="GPS &#25915;&#20987;&#30028;&#38754;">
      </div>
    </div>
    <div class="ui-gallery-card">
      <div class="ui-gallery-title">HackRF &#26816;&#27979;&#30028;&#38754;</div>
      <div class="ui-gallery-frame">
        <img src="{{ '/assets/images/hackrf_detection.png' | relative_url }}" alt="HackRF &#26816;&#27979;&#30028;&#38754;">
      </div>
    </div>
    <div class="ui-gallery-card">
      <div class="ui-gallery-title">HackRF One &#20998;&#26512;&#30028;&#38754;</div>
      <div class="ui-gallery-frame">
        <img src="{{ '/assets/images/hackrf_one_analysis.png' | relative_url }}" alt="HackRF One &#20998;&#26512;&#30028;&#38754;">
      </div>
    </div>
    <div class="ui-gallery-card">
      <div class="ui-gallery-title">MAVLink &#39029;&#38754;</div>
      <div class="ui-gallery-frame">
        <img src="{{ '/assets/images/marvlink_page.png' | relative_url }}" alt="MAVLink &#39029;&#38754;">
      </div>
    </div>
    <div class="ui-gallery-card">
      <div class="ui-gallery-title">&#20449;&#21495;&#21457;&#23556;&#30028;&#38754;</div>
      <div class="ui-gallery-frame">
        <img src="{{ '/assets/images/signal_send.png' | relative_url }}" alt="&#20449;&#21495;&#21457;&#23556;&#30028;&#38754;">
      </div>
    </div>
    <div class="ui-gallery-card">
      <div class="ui-gallery-title">YOLO &#39029;&#38754;</div>
      <div class="ui-gallery-frame">
        <img src="{{ '/assets/images/yolo_page.png' | relative_url }}" alt="YOLO &#39029;&#38754;">
      </div>
    </div>
  </div>
</div>
---

<div id="sec-tech"></div>
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
<div id="sec-arch"></div>
## 🏗️ 系统架构

<div class="arch-top-nav">
  <a href="#arch-31">3.1 总体架构</a>
  <a href="#arch-32">3.2 感知层</a>
  <a href="#arch-33">3.3 传输层</a>
  <a href="#arch-34">3.4 处理层</a>
  <a href="#arch-35">3.5 决策层</a>
  <a href="#arch-36">3.6 扩展层</a>
  <a href="#arch-37">3.7 数据流</a>
</div>

<div class="arch-shell">
<aside class="arch-sidebar">
  <h4>目录</h4>
  <div class="arch-sidebar-links">
    <a href="#arch-31">3.1 总体架构分层</a>
    <a href="#arch-32">3.2 感知层</a>
    <a href="#arch-33">3.3 传输层</a>
    <a href="#arch-34">3.4 处理层</a>
    <a href="#arch-35">3.5 决策层</a>
    <a href="#arch-36">3.6 扩展层</a>
    <a href="#arch-37">3.7 数据流说明</a>
  </div>
</aside>
<div class="arch-main">

<h3 id="arch-31">3.1 总体架构分层</h3>

系统采用五层纵深防御架构，各层间通过标准化接口解耦，支持横向扩展与组件热插拔。

<div class="layer-stack">
  <div class="layer-row">◇ 扩展层 <em>REST / gRPC / SDK</em></div>
  <div class="layer-row">◆ 决策层 <em>规则引擎 / RL</em></div>
  <div class="layer-row">▣ 处理层 <em>GUI / 存储 / 加速</em></div>
  <div class="layer-row">▤ 传输层 <em>ZeroMQ / SSH</em></div>
  <div class="layer-row">◉ 感知层 <em>SDR / 视觉 / 雷达</em></div>
</div>

<p align="center">
  <img src="{{ '/assets/images/image.png' | relative_url }}" alt="系统整体架构图" width="920">
</p>
<p align="center">系统整体架构</p>

<h3 id="arch-32">3.2 感知层</h3>

<div class="arch-grid">
  <div class="arch-card">
    <h4>◉ SDR 传感器节点</h4>
    <p>RTL-SDR / HackRF One / PlutoSDR 组合部署。</p>
    <p>支持 3–8 节点分布式组网，GPS 授时纳秒级同步。</p>
    <p>AGC 自适应增益控制，动态范围 ≥ 80 dB。</p>
  </div>
  <div class="arch-card">
    <h4>▦ 视觉传感器</h4>
    <p>工业级 IP 摄像机，H.265 1080p@30fps，RTSP/ONVIF。</p>
    <p>Jetson AGX Orin 部署 YOLO 页面v8s（TensorRT），检测 ≥ 30 FPS。</p>
  </div>
  <div class="arch-card">
    <h4>◇ 辅助传感器</h4>
    <p>气象站用于修正信号传播模型。</p>
    <p>频谱监测仪（选配）用于 SDR 精度校验。</p>
  </div>
</div>

<h3 id="arch-33">3.3 传输层</h3>

<div class="arch-grid">
  <div class="arch-card">
    <h4>▤ 低延迟消息总线</h4>
    <p>基于 ZeroMQ PUB/SUB，节点通信延迟 &lt; 10 ms。</p>
    <p>IQ 数据与控制指令使用 Protobuf 序列化，压缩比约 3:1。</p>
  </div>
  <div class="arch-card">
    <h4>◆ 远程控制通道</h4>
    <p>Paramiko SSH 架构远程配置 HackRF 等设备。</p>
    <p>支持 USB-over-IP、REST/ZeroRPC，API 兼容 pyhackrf。</p>
  </div>
  <div class="arch-card">
    <h4>◈ 视频流传输</h4>
    <p>GStreamer 推送 H.264 视频到 GUI，WebRTC 可选。</p>
    <p>端到端延迟 ≤ 200 ms。</p>
  </div>
</div>

<h3 id="arch-34">3.4 处理层</h3>

<div class="arch-grid">
  <div class="arch-card">
    <h4>▣ 图形用户界面</h4>
    <p>PyQt6 + QML，支持深浅主题切换。</p>
    <p>Matplotlib + PyQtGraph 实时渲染，频谱帧率 ≥ 25 FPS。</p>
    <p>Leaflet.js + QWebEngineView 实现实时地图标绘。</p>
  </div>
  <div class="arch-card">
    <h4>◐ 信号处理加速</h4>
    <p>FFT/FIR/相关运算通过 Cython 或 Numba 加速。</p>
    <p>多进程并行扫描，多核 CPU 任务分发。</p>
  </div>
  <div class="arch-card">
    <h4>⬒ 持久化存储</h4>
    <p>开发期 JSON，生产期自动切换 SQLite。</p>
    <p>原始 IQ 用 HDF5 归档，支持 TB 级并保留元数据。</p>
  </div>
</div>

<h3 id="arch-35">3.5 决策层</h3>

<div class="arch-grid">
  <div class="arch-card">
    <h4>◆ 规则引擎</h4>
    <p>基于 Rete 的轻量规则库，预置 50+ 威胁规则。</p>
    <p>支持在 GUI 中动态增删规则。</p>
  </div>
  <div class="arch-card">
    <h4>◉ 机器学习推理</h4>
    <p>TensorFlow Lite 本地推理：模型 &lt; 10 MB，CPU 单次 &lt; 15 ms。</p>
    <p>ONNX Runtime + CUDA 在 Jetson 推理 &lt; 5 ms。</p>
  </div>
  <div class="arch-card">
    <h4>◇ 策略管理</h4>
    <p>DQN 在线/离线训练生成干扰策略，参数持久化到 SQLite。</p>
    <p>支持自定义波形与发射时序，下发到 HackRF。</p>
  </div>
</div>

<h3 id="arch-36">3.6 扩展层</h3>

<div class="arch-grid">
  <div class="arch-card">
    <h4>▤ API 接口</h4>
    <p>RESTful API（Flask）提供状态查询、威胁检索与干扰控制。</p>
    <p>gRPC 支持高性能跨语言调用（C++/Java/Go）。</p>
  </div>
  <div class="arch-card">
    <h4>▣ Python SDK</h4>
    <p>封装频谱获取、识别与定位能力。</p>
    <p>提供最小化接入示例，便于第三方扩展。</p>
  </div>
  <div class="arch-card">
    <h4>◈ 系统集成</h4>
    <p>支持 Modbus TCP 对接电子围栏。</p>
    <p>支持 Syslog 转发告警到安防中心。</p>
  </div>
</div>

<h3 id="arch-37">3.7 数据流说明</h3>

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

</div>
</div>

---

<div id="sec-metrics"></div>
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
| **页面加载性能** | 首次启动 26.7 s，后续平均 8.6 s | 瓶颈为 YOLO 页面 模型加载，已优化为异步预加载 |
| **最大 IQ 记录速率** | 80 MB/s | HDF5 直接写入，无丢包 |

---

<div id="sec-stack"></div>
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
| **协议分析** | Scapy | WiFi/MAVLink 页面 包构造 | 灵活、可编程 |
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

<div id="sec-meta"></div>
## 📦 版本与信息

- **当前版本**：1.0.0（初始稳定版）  
- **发布日期**：2025 年 12 月  
- **开发团队**：Xuhui Li, Qixin Duan  
- **联系邮箱**：lixuhui25@mails.ucas.ac.cn  
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

---

---
