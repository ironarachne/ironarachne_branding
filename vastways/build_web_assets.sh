#!/usr/bin/env bash
# Render the checked-in Vastways web icon and social-card SVGs.
set -euo pipefail

brand="$(cd "$(dirname "$0")" && pwd)"
icons="$brand/web-icons"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

rsvg-convert -w 180 -h 180 "$icons/favicon.svg" -o "$icons/apple-touch-icon.png"
for size in 192 512; do
  rsvg-convert -w "$size" -h "$size" "$icons/favicon.svg" -o "$icons/vastways-icon-$size.png"
done
for size in 16 32 48; do
  rsvg-convert -w "$size" -h "$size" "$icons/favicon.svg" -o "$work/favicon-$size.png"
done

magick "$work/favicon-16.png" "$work/favicon-32.png" "$work/favicon-48.png" "$icons/favicon.ico"
rsvg-convert "$brand/logo/vastways-social.svg" -o "$icons/vastways-social.png"
