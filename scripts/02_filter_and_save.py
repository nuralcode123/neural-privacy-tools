#!/usr/bin/env python3
"""
02_filter_and_save.py
---------------------
Stage 1 - Script 2: Apply a simple band-pass filter and save the cleaned data locally.

Everything stays on your machine. The cleaned file is written to data/processed/.
Includes plain-language transparency logging.
"""

import mne
from pathlib import Path
from datetime import datetime

# -------------------------------------------------
# Configuration
# -------------------------------------------------
INPUT_PATH  = Path("data/examples/sample_audvis_raw.fif")
OUTPUT_PATH = Path("data/processed/sample_filtered_raw.fif")

# Filter settings (common starting point for EEG)
L_FREQ = 1.0    # high-pass (Hz) – removes slow drifts / DC offset
H_FREQ = 40.0   # low-pass (Hz)  – removes high-frequency noise

def log_status(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def main():
    print("=" * 70)
    print("Neural Privacy Tools  ·  Filter & Save  ·  Local-Only")
    print("=" * 70)
    log_status("Starting filter. All processing stays on this machine.")

    if not INPUT_PATH.exists():
        log_status(f"Input file not found: {INPUT_PATH}")
        print("Run 01_load_data.py first or place a raw file in data/examples/")
        return

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    log_status(f"Loading raw data from {INPUT_PATH.name}")
    raw = mne.io.read_raw(INPUT_PATH, preload=True, verbose=False)

    log_status(f"Applying band-pass filter: {L_FREQ}–{H_FREQ} Hz")
    log_status("Plain language: Removing very slow drifts (below 1 Hz) and high-frequency noise (above 40 Hz).")
    raw_filtered = raw.copy().filter(l_freq=L_FREQ, h_freq=H_FREQ, verbose=False)

    log_status(f"Saving cleaned data locally to {OUTPUT_PATH}")
    raw_filtered.save(OUTPUT_PATH, overwrite=True, verbose=False)

    size_mb = OUTPUT_PATH.stat().st_size / 1e6
    print("\n--- Summary ---")
    print(f"Original sampling rate : {raw.info['sfreq']} Hz")
    print(f"Filter applied         : {L_FREQ}–{H_FREQ} Hz band-pass")
    print(f"Output file            : {OUTPUT_PATH}")
    print(f"File size              : {size_mb:.1f} MB")

    log_status("Filtered data saved. Original raw file was left untouched.")
    log_status("Status: No data left the machine.")
    print("=" * 70)

if __name__ == "__main__":
    main()
