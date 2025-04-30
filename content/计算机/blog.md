---
title: 博客搭建
---

# [quartz](https://quartz.jzhao.xyz/) 博客搭建流程

## Install

```bash
git clone https://github.com/jackyzha0/quartz.git
cd quartz
npm i
npx quartz create
```

## 修改配置

修改 `quartz.config.ts` 里的`baseUrl`

```ts
    baseUrl: "${github_username}.github.io",
```

## 同步github

```
git remote set-url origin {REMOTE-URL}
npx quartz sync --no-pull
```

## 部署到 GitHub Pages

(执行完这一步才能在 `{github_username}.github.io` 看到博客的网页)

In your local Quartz, create a new file quartz/.github/workflows/deploy.yml.

```yaml
name: Deploy Quartz site to GitHub Pages

on:
  push:
    branches:
      - v4

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Fetch all history for git info
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - name: Install Dependencies
        run: npm ci
      - name: Build Quartz
        run: npx quartz build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: public

  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## 参考资料

```
https://quartz.jzhao.xyz/
```
