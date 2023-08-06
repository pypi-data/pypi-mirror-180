#!/bin/bash

file="/etc/xdg/autostart/sun_daemon.desktop.sample"
if [ -r $file ]; then
  mv $file "/etc/xdg/autostart/$(basename $file .sample)"
  echo "SUN daemon autostart enabled."
fi
