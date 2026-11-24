import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { registerCondition } from "./quartz/plugins/loader/conditions"
import { componentRegistry } from "./quartz/components/registry"
import type { QuartzComponent } from "./quartz/components/types"

// Recent Notes - start====================================
import type { QuartzPluginData } from "./quartz/plugins/vfile"

registerCondition("is-updates-page", (props) => props.fileData.slug === "updates")
registerCondition("not-updates-page", (props) => props.fileData.slug !== "updates")

componentRegistry.setOptionOverrides("quartz-v5-plugin-recent-notes", {
  filter: (f: QuartzPluginData) => {
    const slug = f.slug ?? ""
    return (
      slug !== "updates" &&
      slug !== "404" &&
      slug !== "dependency_graph" &&
      !slug.endsWith("/dependency_graph")
    )
  },
})

// Recent Notes - end====================================

// Top Card 滚动收起 - start ===============================
// 只带 afterDOMLoaded 的"空组件"：组件不会被渲染，但 componentResources 会
// 收集它的脚本并全局注入（和配置里 position: body 的插件同一机制）。
const topCardScroll: QuartzComponent = () => null

topCardScroll.afterDOMLoaded = `
document.addEventListener("nav", () => {
  const root = document.documentElement
  const HIDE_AFTER = 80
  const MIN_DELTA = 6

  const setHidden = (hidden) => {
    root.classList.toggle("topcard-hidden", hidden)
  }

  let lastY = window.scrollY
  let ticking = false

  const update = () => {
    ticking = false
    const y = Math.max(window.scrollY, 0)
    const dy = y - lastY
    if (Math.abs(dy) < MIN_DELTA) return
    lastY = y

    // 顶部永远展开
    if (y <= 8) {
      setHidden(false)
      return
    }
    // 搜索面板打开时不要把导航条收走
    if (document.querySelector(".search-container.active")) {
      setHidden(false)
      return
    }
    setHidden(dy > 0 && y > HIDE_AFTER)
  }

  const onScroll = () => {
    if (ticking) return
    ticking = true
    requestAnimationFrame(update)
  }

  setHidden(false)
  window.addEventListener("scroll", onScroll, { passive: true })
  window.addCleanup(() => window.removeEventListener("scroll", onScroll))
})
`

componentRegistry.register("top-card-scroll", () => topCardScroll, "quartz.ts")
// Top Card 滚动收起 - end =================================

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
