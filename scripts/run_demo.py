#!/usr/bin/env python3
"""
run_demo.py
-----------
Single-command demo of Neural Privacy Tools.

Loads a local EEG file, applies a simple filter, runs a basic artifact check,
and writes a plain-language log. Nothing leaves the machine.
"""

import sys
from pathlib import Path

# Make the transparency logger importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from transparency.logger import log_status, log_privacy_affirmation

def main():
    print("=" * 72)
    print("  Neural Privacy Tools  ·  Local-First Demo  ·  Nothing leaves this machine")
    print("=" * 72)
    log_status("Starting demo pipeline. All processing stays on this computer.", step="pipeline")

    scripts_dir = Path(__file__).parent

    steps = [
        ("01_load_data.py", "load"),
        ("02_filter_and_save.py", "filter"),
        ("04_artifact_check.py", "artifact"),
        ("03_plot_before_after.py", "plot"),
    ]

    for script, step_name in steps:
        log_status(f"Running step: {step_name}", step=step_name)
        result = subprocess_run(scripts_dir / script)
        if result != 0:
            log_status(f"Step {step_name} stopped (exit code {result}).", step=step_name, level="ERROR")
            break
        log_privacy_affirmation(step_name)

    log_status("Demo finished. Full plain-language record is in data/logs/pipeline.log", step="pipeline")
    print("\nYou can inspect the log with:")
    print("  cat data/logs/pipeline.log")
    print("=" * 72)

def subprocess_run(script_path):
    import subprocess
    result = subprocess.run([sys.executable, str(script_path)], capture_output=False)
    return result.returncode

if __name__ == "__main__":
    main()
