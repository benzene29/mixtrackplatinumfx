#!/bin/bash
# Simple installer for MixTrack Platinum FX initializer

# Setup paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LAUNCH_AGENT_DIR="$HOME/Library/LaunchAgents"
LAUNCH_AGENT_NAME="com.mixtrack.initializer.plist"
LAUNCH_AGENT_PATH="$LAUNCH_AGENT_DIR/$LAUNCH_AGENT_NAME"
TEMPLATE_PATH="$SCRIPT_DIR/com.mixtrack.monitor.plist"

# Install required dependencies
echo "Installing required Python modules..."
pip3 install python-rtmidi

# Create LaunchAgents directory
mkdir -p "$LAUNCH_AGENT_DIR"

# Create a fully customized version of the plist with the current path
sed -e "s|SCRIPT_PATH_PLACEHOLDER|$SCRIPT_DIR|g" "$TEMPLATE_PATH" > "$LAUNCH_AGENT_PATH"

# Unload the agent if it exists
launchctl unload "$LAUNCH_AGENT_PATH" 2>/dev/null

# Set proper permissions
chmod 644 "$LAUNCH_AGENT_PATH"

# Load the agent
launchctl load "$LAUNCH_AGENT_PATH"

echo "✅ MixTrack Platinum FX autorunner installed!"
echo "The script will run automatically when you connect your controller."
echo "Check logs at: /tmp/mixtrack-initializer.log"
