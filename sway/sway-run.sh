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

# Set dependencies to run with proprietary drivers
if grep -qE "nvidia|fglrx" /proc/modules; then
	export WLR_NO_HARDWARE_CURSORS=1
	unsupported_gpu="--unsupported-gpu"
else
	unsupported_gpu=""
fi

# Start the Sway session
systemctl --user start sway-session.target

systemd-cat --identifier=sway sway $unsupported_gpu $@
