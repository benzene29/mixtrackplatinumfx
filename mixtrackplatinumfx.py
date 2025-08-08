import rtmidi
import time

midiout = rtmidi.MidiOut()

available_ports = midiout.get_ports()

if "MixTrack Platinum FX" in available_ports:
    midiout.open_port(available_ports.index("MixTrack Platinum FX"))
else:
    print(f"Port 'MixTrack Platinum FX' not found.")
    exit(1)

# Codes to send to the MixTrack Platinum FX
# Found by istankovic https://mixxx.discourse.group/t/numark-mixtrack-pro-fx/19561/7

midiout.send_message([0xf0, 0x00, 0x20, 0x7f, 0x03, 0x01, 0xf7])
midiout.send_message([0xf0, 0x00, 0x20, 0x7f, 0x04, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf7]) 
midiout.send_message([0xf0, 0x7e, 0x00, 0x06, 0x01, 0xf7])





