-- Network Manager
hl.window_rule({
    name = "com.network.manager",
    match = {class = "com.network.manager"},
    float = true,
    center = true,
    size = "800 600"
})

hl.window_rule({
    match = { class = "org.gnome.NautilusPreviewer" },
    float = true,
    center = true,
    size = "740 470"
})  

hl.window_rule({
  name = "kando",
  match = {
      class = "menu.kando.Kando",
      title = "Kando Menu"
  },
  no_blur = true,
  opaque = true,
  move = {0, 0},
  rounding = 0,
  size = { "100%", "100%" },
  border_size = 0,
  no_anim = true,
  float = true,
  pin = true
})  
