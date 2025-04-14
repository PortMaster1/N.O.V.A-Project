# Onboard Serup
The Onboard setup for Nova means that everything is handled by one computer inside of Nova's body.

The onboard setup is currently supported on the following:
- Jetson Orin Nano (8GB RAM)

This model is planned to be split between two Jetson devices, one being the main files, and the other running the `eye_eye_captain/` folder.

# Installation

1. Download and extract or Git-clone this repo to your Jetzon Orin NX or Orin Nano
2. cd into this folder in a terminal
3. Run `pip install -r requirements.txt` to install dependencies
4. Run `python3 main.py`

### If using a bluetooth speaker:
#### Step 1: Setup Bluetooth on your device
Install required bluetooth adapters
```bash
sudo apt update
sudo apt install bluetooth bluez pulseaudio pulseaudio-module-bluetooth pavucontrol
```
Start and enable bluetooth
```bash
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
```
Pair and trust your device
```bash
bluetoothctl
power on
agent on
default-agent
scan on  # Wait for your speaker to show
pair <MAC_ADDRESS>
trust <MAC_ADDRESS>
connect <MAC_ADDRESS>
quit
```
#### Step 2: Set up PulseAudio to handle the bluetooth audio
Once the bluetooth device is connected:
```bash
pactl list sources short
pactl list sinks short
```
- You should see your Bluetooth speaker as a **sink** and the microphone as a **source** (might be named something like 'bluez_source...' and 'bluez_sink...').
Setup the default audio source and sink:
```bash
pactl set-default-sink <BT_SPEAKER_NAME>
pactl set-default-source <BT_MIC_NAME>
```
#### Step 3: Test Audio
* Test Speaker:
```bash
paplay /usr/share/sounds/alsa/Front_Center.wav
```
* Test Microphone:
```bash
arecord -D <BT_MIC_DEVICE_NAME> -f cd test.wav
aplay test.wav
```

> [!NOTE]
> It takes a while for the model to fully download, so don’t worry if it's taking a long time.
> Once it is downloaded, it is cached so you do not have to download it again the next time you use it.