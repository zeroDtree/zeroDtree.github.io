---
title: Local plugins
---

`my-plugins/` is gitignored. Each plugin is its own GitHub repo. Install and options are documented in that repo's README.

```yaml
- source: github:zeroDtree/quartz-v5-plugin-out-of-date
- source: github:zeroDtree/quartz-v5-plugin-top-card
- source: github:zeroDtree/quartz-v5-plugin-friends
- source: github:zeroDtree/quartz-v5-plugin-recent-notes
```

To edit one, clone it under `my-plugins/` and set `source` to `./my-plugins/quartz-v5-plugin-...`. Run `npm run dev` in the plugin and `npx quartz build --serve` in the site. After pushing, switch `source` back to `github:zeroDtree/...`.
