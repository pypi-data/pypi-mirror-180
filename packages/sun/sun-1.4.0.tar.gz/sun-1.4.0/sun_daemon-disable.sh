#!/bin/bash

file="/etc/xdg/autostart/sun_daemon.desktop"
if [ -r $file ]; then
  mv $file ${file}.sample
  echo "SUN daemon autostart disabled."
fi
