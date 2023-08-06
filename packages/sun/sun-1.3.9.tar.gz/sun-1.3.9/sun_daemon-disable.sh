#!/bin/sh

for file in /etc/xdg/autostart/sun_daemon.desktop ; do
  if [ -r ${file}.sample ]; then
    rm -f $file
  elif [ -r $file ]; then
    mv ${file} ${file}.sample
  fi
done
echo "SUN daemon autostart disabled."
