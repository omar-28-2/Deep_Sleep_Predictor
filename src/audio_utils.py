import numpy as np
import librosa
import os

def extract_audio_stats(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Audio file not found: {path}")
    y, sr = librosa.load(path, sr=None)
    rms = librosa.feature.rms(y=y)[0]
    return {
        "rms_mean": float(np.mean(rms)),
        "rms_std":  float(np.std(rms)),
    }

def count_snore_events(y, sr, threshold):
    rms = librosa.feature.rms(y=y)[0]
    norm = rms / (rms.max() + 1e-8)
    above = norm > threshold
    # count rising edges
    events = int(((above.astype(int)[1:] - above.astype(int)[:-1]) == 1).sum())
    duration_min = len(y) / sr / 60
    return events / max(duration_min, 1e-3)
