#!/bin/bash
# Load the user's home swayidle configuration, if found.
# Otherwise return 1 to default to the openSUSEway configuration.

SWAYIDLE_HOME_CONFIG="$HOME/.config/swayidle/config"
SWAYIDLE_HOME_CONFIG2="$HOME/swayidle/config"

################################################################

# Kill any previous swayidle
pkill -f "swayidle -w"

if [ -f "$SWAYIDLE_HOME_CONFIG" ]; then
    swayidle -w -C "$SWAYIDLE_HOME_CONFIG"
    exit 0
fi
if [ -f "$SWAYIDLE_HOME_CONFIG2" ]; then
    swayidle -w -C "$SWAYIDLE_HOME_CONFIG2"
    exit 0
fi
exit 1
