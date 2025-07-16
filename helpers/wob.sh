#!/bin/bash
# Load the user's home wob configuration, if found.
# Otherwise default to the openSUSEway configuration.

set -uo pipefail

WOB_FIFO="$SWAYSOCK.wob"
WOB_HOME_CONFIG="$HOME/.config/wob/wob.ini"
WOB_OPENSUSEWAY_CONFIG="/etc/sway/wob/wob.ini"

################################################################

# Kill any previous wob listener
pkill -f "tail -f $WOB_FIFO"

# Create the wob fifo if not found
test -e "$WOB_FIFO" || mkfifo "$WOB_FIFO"

if [ -f "$WOB_HOME_CONFIG" ]; then
    tail -f "$WOB_FIFO" | wob --config "$WOB_HOME_CONFIG"
else
    tail -f "$WOB_FIFO" | wob --config "$WOB_OPENSUSEWAY_CONFIG"
fi
