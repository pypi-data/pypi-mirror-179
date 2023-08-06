#!/bin/sh

for file in /etc/xdg/autostart/sun_daemon.desktop.sample ; do
  if [ -r $file ]; then
    mv $file /etc/xdg/autostart/$(basename $file .sample)
  fi
done
echo "SUN daemon autostart enabled."
