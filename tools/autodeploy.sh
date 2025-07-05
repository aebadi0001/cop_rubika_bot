#!/usr/bin/env bash

# ابزاری ساده برای نظارت روی تغییرات
# نیاز به inotify-tools در ترموکس:
# pkg install inotify-tools

WATCHED="bot vendor FEATURES.md"

while inotifywait -e modify,create,delete -r $WATCHED; do
  git add .
  git commit -m "Auto: code update $(date '+%Y-%m-%d %H:%M:%S')" --no-verify || true
  git push origin main
done
