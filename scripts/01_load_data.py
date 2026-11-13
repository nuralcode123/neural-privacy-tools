#!/usr/bin/env python3
"""
01_load_data.py
---------------
Stage 1 - Script 1: Load a public EEG dataset and print basic information.

This script stays completely local. It only reads data and prints summary info.
No data is sent anywhere.
"""

import mne
from pathlib import Path
from datetime import datetime

# -------------------------------------------------
# Configuration (edit these paths if needed)
# -------------------------------------------------
DATA_PATH = Path("data/examples/sample_audvis_raw.fif")  # MNE sample data

def log_status(message: str):
    """Plain-language status log. Always local."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def main():
    print("=" * 70)
    print("Neural Privacy Tools  ·  Load Data  ·  Local-Only")
    print("=" * 70)
    log_status("Starting load. Nothing leaves this machine.")

    if not DATA_PATH.exists():
        log_status(f"File not found: {DATA_PATH}")
        print("\nTo get the MNE sample dataset, run this once in Python:")
        print("    import mne")
        print("    mne.datasets.sample.data_path()")
        print("\nThen copy sample_audvis_raw.fif into data/examples/")
        print("Or point DATA_PATH to any local .fif / .edf / .bdf file.")
        return

    log_status(f"Opening file: {DATA_PATH.name}")
    raw = mne.io.read_raw(DATA_PATH, preload=False, verbose=False)

    print("\n--- Basic Info ---")
    print(f"File name         : {DATA_PATH.name}")
    print(f"Sampling rate     : {raw.info['sfreq']} Hz")
    print(f"Number of channels: {len(raw.ch_names)}")
    print(f"First 10 channels : {raw.ch_names[:10]}")
    print(f"Duration          : {raw.times[-1]:.1f} seconds")
    print(f"High-pass filter  : {raw.info['highpass']} Hz")
    print(f"Low-pass filter   : {raw.info['lowpass']} Hz")

    print("\n--- Channel Types ---")
    types = raw.get_channel_types()
    unique = sorted(set(types))
    print(f"Types present: {', '.join(unique)}")

    log_status("Data loaded successfully. Original file was not modified.")
    log_status("Status: Nothing was uploaded or sent anywhere.")
    print("=" * 70)

if __name__ == "__main__":
    main()
