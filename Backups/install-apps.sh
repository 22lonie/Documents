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
  nano\
  nmap \
  openssh \
  rhythmbox\
  ttf-jetbrains-mono\
  ttf-jetbrains-mono-nerd\
  yt-dlp

echo "==> Installing AUR packages..."
yay -S --needed \
  zapzap \
  superproductivity \
  brave-bin \
  visual-studio-code-bin\
  spotify

echo "==> Done!"
