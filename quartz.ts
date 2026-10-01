import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { registerCondition } from "./quartz/plugins/loader/conditions"
import { componentRegistry } from "./quartz/components/registry"

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

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
