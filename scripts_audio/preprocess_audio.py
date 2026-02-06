"""
Audio Preprocessing: Crossfade-Looping + Volume Normalization
for "Die Stille von Graubach"

Uses scipy.io.wavfile to handle float32 WAV files from AudioCraft.
Outputs 16-bit PCM WAV for Godot compatibility.

- Music (12 files, 30s, 32kHz): 3s crossfade, -14 dBFS
- Ambience (5 files, 10s, 16kHz): 2s crossfade, -20 dBFS
- SFX (10 files): no crossfade, -12 dBFS
- Backup to assets/audio/backup/ before processing
"""

import os
import shutil
import math
import sys
import numpy as np
from scipy.io import wavfile

AUDIO_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "audio")
BACKUP_DIR = os.path.join(AUDIO_ROOT, "backup")

CATEGORIES = {
    "music":    {"crossfade_sec": 3.0, "target_dbfs": -14.0},
    "ambience": {"crossfade_sec": 2.0, "target_dbfs": -20.0},
    "sfx":      {"crossfade_sec": 0.0, "target_dbfs": -12.0},
}


def read_wav(path):
    """Read WAV file, return (sample_rate, data as float64 numpy array, shape: (frames,) or (frames, channels))."""
    sample_rate, data = wavfile.read(path)
    # Convert to float64 in range [-1.0, 1.0]
    if data.dtype == np.float32 or data.dtype == np.float64:
        data = data.astype(np.float64)
    elif data.dtype == np.int16:
        data = data.astype(np.float64) / 32768.0
    elif data.dtype == np.int32:
        data = data.astype(np.float64) / 2147483648.0
    else:
        raise ValueError(f"Unsupported dtype: {data.dtype}")
    return sample_rate, data


def write_wav_16bit(path, sample_rate, data):
    """Write as 16-bit PCM WAV (Godot-compatible)."""
    # Clip and convert to int16
    data = np.clip(data, -1.0, 1.0)
    data_int16 = (data * 32767.0).astype(np.int16)
    wavfile.write(path, sample_rate, data_int16)


def compute_rms_dbfs(data):
    """Compute RMS level in dBFS from float64 data in [-1, 1]."""
    rms = np.sqrt(np.mean(data ** 2))
    if rms < 1e-10:
        return -100.0
    return 20.0 * math.log10(rms)


def normalize(data, current_dbfs, target_dbfs):
    """Apply gain to reach target dBFS."""
    if current_dbfs <= -100.0:
        return data
    gain_db = target_dbfs - current_dbfs
    gain_linear = 10.0 ** (gain_db / 20.0)
    return data * gain_linear


def apply_crossfade(data, sample_rate, crossfade_sec):
    """Apply crossfade looping: mix tail into head for seamless loop."""
    if crossfade_sec <= 0:
        return data

    is_mono = data.ndim == 1
    total_frames = data.shape[0]
    crossfade_frames = int(crossfade_sec * sample_rate)

    if crossfade_frames >= total_frames // 2:
        crossfade_frames = total_frames // 4
        print(f"    Warning: crossfade shortened to {crossfade_frames / sample_rate:.1f}s")

    # Extract tail region
    tail = data[-crossfade_frames:].copy()

    # Trim audio (remove tail)
    trimmed = data[:-crossfade_frames].copy()

    # Create fade curves
    fade_in = np.linspace(0.0, 1.0, crossfade_frames)
    fade_out = np.linspace(1.0, 0.0, crossfade_frames)

    if not is_mono:
        fade_in = fade_in[:, np.newaxis]
        fade_out = fade_out[:, np.newaxis]

    # Mix tail into head
    trimmed[:crossfade_frames] = trimmed[:crossfade_frames] * fade_in + tail * fade_out

    return trimmed


def process_file(filepath, category_config):
    """Process a single WAV file with crossfade and normalization."""
    filename = os.path.basename(filepath)
    crossfade_sec = category_config["crossfade_sec"]
    target_dbfs = category_config["target_dbfs"]

    print(f"  Processing: {filename}")

    sample_rate, data = read_wav(filepath)
    n_channels = 1 if data.ndim == 1 else data.shape[1]
    duration = data.shape[0] / sample_rate

    print(f"    Input: {sample_rate}Hz, {n_channels}ch, {duration:.1f}s")

    # Step 1: Crossfade
    if crossfade_sec > 0:
        original_frames = data.shape[0]
        data = apply_crossfade(data, sample_rate, crossfade_sec)
        new_duration = data.shape[0] / sample_rate
        print(f"    Crossfade: {crossfade_sec}s ({duration:.1f}s -> {new_duration:.1f}s)")

    # Step 2: Normalize
    current_dbfs = compute_rms_dbfs(data)
    data = normalize(data, current_dbfs, target_dbfs)
    new_dbfs = compute_rms_dbfs(data)
    print(f"    Volume: {current_dbfs:.1f} -> {new_dbfs:.1f} dBFS (target: {target_dbfs:.1f})")

    # Write back as 16-bit PCM
    write_wav_16bit(filepath, sample_rate, data)
    print(f"    Written as 16-bit PCM.")


def backup_all():
    """Backup all audio files before processing."""
    print("=== Backing up audio files ===")
    for category in CATEGORIES:
        src_dir = os.path.join(AUDIO_ROOT, category)
        dst_dir = os.path.join(BACKUP_DIR, category)
        os.makedirs(dst_dir, exist_ok=True)
        for fname in sorted(os.listdir(src_dir)):
            if fname.endswith(".wav"):
                src = os.path.join(src_dir, fname)
                dst = os.path.join(dst_dir, fname)
                if not os.path.exists(dst):
                    shutil.copy2(src, dst)
                    print(f"  Backed up: {category}/{fname}")
                else:
                    print(f"  Already backed up: {category}/{fname}")
    print()


def main():
    print("=" * 60)
    print("Audio Preprocessing: Die Stille von Graubach")
    print("=" * 60)
    print()

    if not os.path.isdir(AUDIO_ROOT):
        print(f"ERROR: Audio directory not found: {AUDIO_ROOT}")
        sys.exit(1)

    # Step 1: Backup
    backup_all()

    # Step 2: Process each category
    total_processed = 0
    for category, config in CATEGORIES.items():
        cat_dir = os.path.join(AUDIO_ROOT, category)
        if not os.path.isdir(cat_dir):
            print(f"Skipping {category}: directory not found")
            continue

        wav_files = sorted(f for f in os.listdir(cat_dir) if f.endswith(".wav"))
        print(f"=== {category.upper()} ({len(wav_files)} files) ===")
        print(f"    Crossfade: {config['crossfade_sec']}s, Target: {config['target_dbfs']} dBFS")
        print()

        for fname in wav_files:
            filepath = os.path.join(cat_dir, fname)
            process_file(filepath, config)
            total_processed += 1
        print()

    print(f"=== All done! {total_processed} files processed. ===")


if __name__ == "__main__":
    main()
