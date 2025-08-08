#!/usr/bin/env python3
"""
MixTrack Platinum FX Initialization Script
Sends SysEx messages to initialize the controller's LCD and LED lights
"""
import time
import sys
import os
import subprocess

try:
    import rtmidi
except ImportError:
    print("Error: rtmidi module not found, attempting to install...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "python-rtmidi"],
                       check=True, capture_output=True)
        print("Successfully installed rtmidi, retrying import...")
        import rtmidi
    except Exception as e:
        print(f"Failed to install rtmidi: {e}")
        sys.exit(1)

def initialize_mixtrack():
    """Initialize the MixTrack Platinum FX controller"""
    # Define MIDI messages
    INIT_MESSAGES = [
        [0xf0, 0x00, 0x20, 0x7f, 0x03, 0x01, 0xf7],
        [0xf0, 0x00, 0x20, 0x7f, 0x04, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf7],
        [0xf0, 0x7e, 0x00, 0x06, 0x01, 0xf7]
    ]

    # Create MIDI output
    midi_out = rtmidi.MidiOut()

    # Find MixTrack controller
    port_count = midi_out.get_port_count()
    if port_count == 0:
        print("No MIDI ports available")
        return False

    available_ports = [midi_out.get_port_name(i) for i in range(port_count)]
    print(f"Available MIDI ports: {available_ports}")

    # Find MixTrack port
    mixtrack_port = None
    for i, name in enumerate(available_ports):
        if "MixTrack" in name or "Numark" in name:
            mixtrack_port = i
            break

    if mixtrack_port is None:
        print("MixTrack Platinum FX not found")
        return False

    # Connect and send messages
    try:
        midi_out.open_port(mixtrack_port)
        print(f"Connected to: {available_ports[mixtrack_port]}")

        # Send initialization messages
        print("Sending initialization messages...")
        for msg in INIT_MESSAGES:
            midi_out.send_message(msg)
            time.sleep(0.1)  # Short delay between messages

        print("MixTrack Platinum FX initialized successfully!")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        # Always close the port when done
        if midi_out.is_port_open():
            midi_out.close_port()

if __name__ == "__main__":
    success = initialize_mixtrack()
    sys.exit(0 if success else 1)
