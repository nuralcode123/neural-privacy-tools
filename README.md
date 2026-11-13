# Neural Privacy Tools

**Local-first tools for processing neural (EEG) data with privacy and transparency as the defaults.**

> Your brain data stays on your machine unless you explicitly choose otherwise.  
> Every step is inspectable in plain language.

This is a small, open-source pipeline that loads, filters, and checks EEG data entirely locally while generating human-readable audit logs. It is designed so users and researchers can see exactly what happened to their data without needing deep technical knowledge.

## Why this exists

Consumer and research EEG/BCI tools increasingly process brain data. Many of those pipelines are hard to inspect. Neural Privacy Tools demonstrates a practical alternative: local processing, open code, and plain-language transparency.

## Quick start

```bash
# Install dependencies
pip install -r requirements.txt

# Download a small public sample dataset (one time)
python -c "import mne; mne.datasets.sample.data_path()"

# Copy the sample file into place (adjust path if needed)
# Then run the demo:
python scripts/run_demo.py
```

The demo:
- Loads EEG data locally
- Applies a simple band-pass filter
- Runs a basic artifact check
- Writes a plot
- Logs every step in plain English
- Affirms that nothing left the machine

## What you will see

Console output similar to:

```
[2026-11-13 10:15:22] [INFO] [filter] Removing very slow drifts (below 1 Hz) and high-frequency noise (above 40 Hz).
[2026-11-13 10:15:23] [PRIVACY] [filter] Nothing left this machine. All processing stayed local.
```

A full local log is written to `data/logs/pipeline.log`.

## Project principles

1. **Local-first by default** — no network calls in the core path
2. **Plain-language transparency** — logs a non-expert can read
3. **Original data is never modified**
4. **Open and auditable code**
5. **Built on proven tools** (MNE-Python) rather than reinventing signal processing

## Structure

```
scripts/              # Ready-to-run tools (run_demo.py is the single entry point)
src/transparency/     # Plain-language logger
data/                 # examples/, processed/, logs/ (created at runtime)
```

## Status

Demo-ready local pipeline. Suitable for showing the local-only + plain-language approach in a few minutes. Intended as a practical contribution toward user control of neural data.

## License

MIT License. See [LICENSE](LICENSE).

---

Built so people can keep their brain data under their own control.
