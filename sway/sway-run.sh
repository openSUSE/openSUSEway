#!/bin/sh

# Session
export XDG_SESSION_TYPE=wayland
export XDG_SESSION_DESKTOP=sway
export XDG_CURRENT_DESKTOP=sway

# this file imports openSUSEway desktop enviroments
set -a
. /etc/sway/env
set +a

systemd-cat --identifier=sway sway $@

