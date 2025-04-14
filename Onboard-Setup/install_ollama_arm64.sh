#!/bin/bash
# install_ollama.sh

set -e

# Download Ollama for Arm64
curl -L https://ollama.com/download/ollama-linux-arm64.tgz -o ollama-linux-arm64.tgz
sudo tar -C /usr -xzf ollama-linux-arm64.tgz

# Set Ollama as a startup service
sudo useradd -r -s /bin/false -U -m -d /usr/share/ollama ollama
sudo usermod -a -G ollama $(whoami)

cat <<EOF > /etc/systemd/system/ollama.service

[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=$PATH"

[Install]
WantedBy=multi-user.target
EOF

# Start Ollama
sudo systemctl daemon-reload
sudo systemctl enable ollama

sudo systemctl start ollama
sudo systemctl status ollama

pip install --upgrade pip
pip install -r requirements.txt

echo "Installed Ollama"