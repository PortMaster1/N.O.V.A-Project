#!/usr/bin/env python3

import sys
import os
import subprocess

# === CONFIG ===
DOWNLOAD_DIR = "/path/to/your/download/folder"  # Change this

# === MAIN LOGIC ===
def main():
    if len(sys.argv) != 2:
        print("Usage: download_youtube.py <YouTube-URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Change to target directory
    os.chdir(DOWNLOAD_DIR)

    # Run yt-dlp with mp4 conversion
    command = [
        "yt-dlp",
        "-f", "mp4",  # Prefer mp4 if available
        "--recode", "mp4",  # Force recode if not already mp4
        url
    ]

    try:
        subprocess.run(command, check=True)
        print("Download complete.")
    except subprocess.CalledProcessError:
        print("Error: yt-dlp failed.")

if __name__ == "__main__":
    main()