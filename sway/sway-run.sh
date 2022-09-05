#!/bin/sh

# Session
export XDG_SESSION_TYPE=wayland
export XDG_SESSION_DESKTOP=sway
export XDG_CURRENT_DESKTOP=sway

set -a
# Import openSUSEway environment variables
. /etc/sway/env
# Import user environment variables
. ~/.config/environment.d/*.conf
set +a

systemd-cat --identifier=sway sway $@

