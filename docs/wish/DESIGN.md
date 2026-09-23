# 当前愿望的设计解释

## L0 — 中心愿望

mykcs.github.io 只做一件事：

    打开旧主页链接
    → 不需要理解托管迁移
    → 直接进入当前正式主页

## L1 — 当前身份

- Public compatibility gateway: mykcs/mykcs.github.io
- Private full source: mykcs/personal-homepage
- Canonical/indexable serving host: https://wangrui92.pages.dev
- Academic compatibility gateway: https://wangrui2025.github.io

## L2 — 路由

根入口和未知旧主页路径回到 canonical 根地址；/zh/、/en/、/zh/cv/、/en/cv/ 等已知路由尽量保持对应路径。

不要建立 mykcs.github.io → 另一个兼容网关 → serving host 的链路。

## L3 — 隐私边界

本 Public repository 只保存跳转壳、README、AGENTS 和 Wish。完整 Astro 源码、私有 Git 历史、内部文档、DEV 工具、凭据、未发布研究或私人资产都不进入这里。
