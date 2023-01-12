#!/bin/sh

# Session
export XDG_SESSION_TYPE=wayland
export XDG_SESSION_DESKTOP=sway
export XDG_CURRENT_DESKTOP=sway

set -a
# Import openSUSEway environment variables
. /etc/sway/env
# Import environment.d variables by calling the systemd generator
eval "$(/usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator)"
set +a

systemd-cat --identifier=sway sway $@
