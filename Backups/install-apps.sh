#!/usr/bin/env bash
set -e

echo "==> Updating Arch Linux..."
sudo pacman -Syu --noconfirm

echo "==> Installing official Arch packages..."
sudo pacman -S --needed --noconfirm \
  okular \
  libreoffice-still \
  gnome-calculator \
  gnome-clocks \
  vlc \
  vlc-plugins-all \
  thunderbird \
  gimp \
  nmap \
  openssh \
  yt-dlp

echo "==> Installing AUR packages..."
yay -S --needed \
  zapzap \
  superproductivity \
  brave-bin \
  visual-studio-code-bin

echo "==> Done!"
