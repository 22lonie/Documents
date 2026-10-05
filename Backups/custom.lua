-- Network Manager
hl.window_rule({
    name = "com.network.manager",
    match = {class = "com.network.manager"},
    float = true,
    center = true,
    size = "800 600"
})

hl.window_rule({
    name = "vscode_starting_width",
    match = { class = "code" },
    scrolling_width = 1.0,
})
