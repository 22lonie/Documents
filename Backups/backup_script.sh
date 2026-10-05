#!/usr/bin/env bash

# ============================================================
# ML4W customization script
# Continues running even if a command fails
# ============================================================

FAILED=0

run_step() {
    local description="$1"
    shift

    echo
    echo "▶ $description"

    if "$@"; then
        echo "✓ $description"
    else
        echo "✗ FAILED: $description"
        FAILED=1
    fi
}

# ------------------------------------------------------------
# Remove Firefox and its data
# ------------------------------------------------------------

run_step "Remove Firefox" sudo pacman -Rns --noconfirm firefox

run_step "Remove Firefox profile data" rm -rf "$HOME/.mozilla/firefox"
run_step "Remove Firefox cache" rm -rf "$HOME/.cache/mozilla"

# ------------------------------------------------------------
# Rofi border radius
# ------------------------------------------------------------

run_step "Change Rofi border radius" \
    sed -i 's/2em/0.7em/g' \
    "$HOME/.config/ml4w/settings/rofi-border-radius.rasi"

# ------------------------------------------------------------
# Remove NetworkManager applet
# ------------------------------------------------------------

run_step "Remove NetworkManager applet" \
    sudo pacman -Rns --noconfirm network-manager-applet

# ------------------------------------------------------------
# Set Brave as the browser
# ------------------------------------------------------------

run_step "Set Brave as the browser" \
    sed -i 's/firefox/brave/g' \
    "$HOME/.mydotfiles/com.ml4w.dotfiles.stable/.config/ml4w/settings/browser.sh"

# ------------------------------------------------------------
# Use native Emote instead of Flatpak
# ------------------------------------------------------------

run_step "Use native Emote" \
    sed -i 's|flatpak run com\.tomjwatson\.Emote|emote|g' \
    "$HOME/.mydotfiles/com.ml4w.dotfiles.stable/.config/ml4w/settings/emojipicker.sh"

# ------------------------------------------------------------
# Use native GNOME Calculator instead of Flatpak
# ------------------------------------------------------------

run_step "Use native GNOME Calculator" \
    sed -i 's|flatpak run org\.gnome\.Calculator|gnome-calculator|g' \
    "$HOME/.mydotfiles/com.ml4w.dotfiles.stable/.config/ml4w/settings/calculator.sh"

# ------------------------------------------------------------
# Replace NetworkManager launcher script
# ------------------------------------------------------------

NETWORKMANAGER_SCRIPT="$HOME/.mydotfiles/com.ml4w.dotfiles.stable/.config/ml4w/settings/networkmanager.sh"

create_networkmanager_script() {
    mkdir -p "$(dirname "$NETWORKMANAGER_SCRIPT")"

    cat > "$NETWORKMANAGER_SCRIPT" <<'EOF'
#!/usr/bin/env bash

if ! pgrep -x "nmgui" >/dev/null; then
    nmgui &
fi
EOF

    chmod +x "$NETWORKMANAGER_SCRIPT"
}

run_step "Replace NetworkManager launcher" create_networkmanager_script

# ------------------------------------------------------------
# Final result
# ------------------------------------------------------------

echo
echo "============================================================"

if [[ "$FAILED" -eq 0 ]]; then
    echo "✓ ALL CHANGES APPLIED SUCCESSFULLY"
else
    echo "⚠ SCRIPT FINISHED WITH ERRORS"
    echo "Some changes failed, but the script continued running."
fi

echo "============================================================"

exit "$FAILED"
