import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"

// Recent Notes - start====================================
import type { QuartzPluginData } from "./quartz/plugins/vfile"
import * as ExternalPlugin from "./.quartz/plugins"

ExternalPlugin.RecentNotes({
  filter: (f: QuartzPluginData) => {
    const slug = f.slug ?? ""
    return slug !== "dependency_graph" && !slug.endsWith("/dependency_graph")
  },
})

// Recent Notes - end====================================

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
