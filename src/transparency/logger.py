"""
transparency/logger.py
----------------------
Richer plain-language transparency layer for Neural Privacy Tools.

All logs stay local. Nothing is sent anywhere.
"""

from datetime import datetime
from pathlib import Path

LOG_DIR = Path("data/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def log_status(message: str, step: str = "general", level: str = "INFO") -> str:
    """
    Write a plain-language status message.
    Returns the formatted line so callers can also print it.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [{level}] [{step}] {message}"
    
    # Console
    print(line)
    
    # Local file log
    log_file = LOG_DIR / "pipeline.log"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    
    return line

def log_privacy_affirmation(step: str):
    """Explicit reminder that nothing left the machine."""
    log_status("Nothing left this machine. All processing stayed local.", step=step, level="PRIVACY")

def get_recent_log_summary(n: int = 20) -> str:
    """Return the last N lines of the local log for inspection."""
    log_file = LOG_DIR / "pipeline.log"
    if not log_file.exists():
        return "No log file yet."
    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return "".join(lines[-n:])
