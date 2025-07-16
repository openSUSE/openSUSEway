#!/bin/bash
# Load the user's home SwayNotificationCenter configuration, if found.
# Otherwise default to the openSUSEway configuration.

SWAYNC_HOME_CONFIG="$HOME/.config/swaync/config.json"
SWAYNC_HOME_STYLE="$HOME/.config/swaync/style.css"

SWAYNC_OPENSUSEWAY_CONFIG="/etc/sway/swaync/config.json"
SWAYNC_OPENSUSEWAY_STYLE="/etc/sway/swaync/style.css"

if [ -f "$SWAYNC_HOME_CONFIG" ]; then
    if [ -f "$SWAYNC_HOME_STYLE" ]; then
        swaync --config "$SWAYNC_HOME_CONFIG" --style "$SWAYNC_HOME_STYLE"
    else
        swaync --config "$SWAYNC_HOME_CONFIG" --style "$SWAYNC_OPENSUSEWAY_STYLE"
    fi
else
    if [ -f "$SWAYNC_HOME_STYLE" ]; then
        swaync --config "$SWAYNC_OPENSUSEWAY_CONFIG" --style "$SWAYNC_HOME_STYLE"
    else
        swaync --config "$SWAYNC_OPENSUSEWAY_CONFIG" --style "$SWAYNC_OPENSUSEWAY_STYLE"
    fi
fi
