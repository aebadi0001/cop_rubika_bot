#!/usr/bin/env bash

# مسیر Raw فایل‌ها در ریپوی شما
BASE="https://raw.githubusercontent.com/aebadi0001/coprubikabot/main/vendor/rubpy"

# پوشه خروجی
mkdir -p ../all_py

# خواندن لیست فایل‌ها
while read -r path; do
  # برداشتن پیشوند vendor/rubpy/
  rel=${path#vendor/rubpy/}

  # ساخت نام فایل خروجی با جایگزینی / به _
  out="../all_py/${rel//\//_}"

  # دانلود نسخه خام
  curl -s "$BASE/$rel" -o "$out"

  echo "Downloaded $rel → $out"
done < ../all_py/file_list.txt