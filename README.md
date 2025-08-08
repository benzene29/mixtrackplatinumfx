# MixTrack Platinum FX Initializer

A simple Python script that initializes the Numark MixTrack Platinum FX controller to prevent it from being in demo mode.

## What it does

This utility sends the necessary MIDI SysEx messages to your MixTrack Platinum FX controller when it's connected, ensuring:
- The LCD screen displays properly
- LED lights work correctly
- The controller isn't stuck in demo mode

## Installation (macOS)

```bash
# Clone this repository
git clone https://github.com/yourusername/mixtrackplatinumfx.git
cd mixtrackplatinumfx

# Install dependencies
pip install -r requirements.txt

# Make the script executable
chmod +x install_macos.sh

# Run the installer
./install_macos.sh
```

That's it! Your MixTrack Platinum FX will now be automatically initialized whenever you connect it.

## How it works

The installer creates a macOS LaunchAgent that:
1. Detects when you connect your MixTrack Platinum FX controller
2. Automatically runs the initialization script
3. Unloads itself after successful initialization

## Manual usage

If you prefer to run the script manually:

```bash
python mixtrackplatinumfx.py
```

## Troubleshooting

If your controller isn't being detected:

1. Check if it's properly connected via USB
2. Make sure it appears in macOS Audio MIDI Setup
3. Check the logs: `cat /tmp/mixtrack-initializer.log`

## Credits

- SysEx initialization codes discovered by [istankovic](https://mixxx.discourse.group/t/numark-mixtrack-pro-fx/19561/7)

## License

MIT
