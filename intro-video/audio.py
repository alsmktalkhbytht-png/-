"""Synthesised soundtrack for the BIOS intro (10 s): riser -> impact -> shimmer -> pad -> two chimes -> fade."""
import sys, wave
import numpy as np

SR, DUR = 44100, 10.0
t = np.arange(int(SR * DUR)) / SR
rng = np.random.default_rng(3)
out = np.zeros((len(t), 2))


def env(a, b, attack=0.02, release=0.3):
    """0..1 envelope that is on between a and b seconds."""
    e = np.clip((t - a) / attack, 0, 1) * np.clip((b - t) / release, 0, 1)
    return e * ((t >= a) & (t <= b))


def lowpass(x, k):
    return np.convolve(x, np.ones(k) / k, mode="same")


# 1) riser whoosh 0.2-1.2 s: noise getting brighter and louder
noise = rng.standard_normal(len(t))
r = np.clip((t - 0.2) / 1.0, 0, 1)
riser = (noise - lowpass(noise, 40)) * (r ** 2.2) * (t < 1.22)
out += 0.22 * np.stack([riser, np.roll(riser, 90)], 1)

# 2) impact at 1.2 s: sub drop + noise burst
d = t - 1.2
hit = (d >= 0) * (np.sin(2 * np.pi * (55 - 20 * np.clip(d, 0, 1)) * d) * np.exp(-d * 3.2)
                  + 0.5 * lowpass(noise, 6) * np.exp(-d * 18))
out += 0.75 * np.stack([hit, hit], 1)

# 3) shimmer 1.3-3.5 s: rising bell partials (D major-ish)
for i, f in enumerate([1174.7, 1480.0, 1760.0, 2349.3, 2960.0]):
    a = 1.3 + i * 0.12
    dd = t - a
    tone = (dd >= 0) * np.sin(2 * np.pi * f * dd) * np.exp(-dd * 2.6)
    pan = 0.3 + 0.1 * i
    out += 0.07 * np.stack([tone * (1 - pan), tone * pan], 1)

# 4) warm pad 1.2-10 s: D minor 9 chord with slow swell and gentle chorus
pad = np.zeros(len(t))
for f in [73.42, 110.0, 146.83, 174.61, 220.0, 329.63]:
    pad += np.sin(2 * np.pi * f * t) + 0.6 * np.sin(2 * np.pi * f * 1.003 * t + 1.0)
pad = lowpass(pad, 30) / 8
pad *= np.clip((t - 1.2) / 2.0, 0, 1) * np.clip((10.0 - t) / 1.2, 0, 1)
out += 0.32 * np.stack([pad, np.roll(pad, 300)], 1)

# 5) soft whoosh at 5.4 s (logo moves up)
w = np.exp(-((t - 5.8) / 0.35) ** 2) * (noise - lowpass(noise, 12))
out += 0.10 * np.stack([np.roll(w, 120), w], 1)

# 6) chimes for each credit card
for a, notes in [(6.1, [880.0, 1318.5]), (7.0, [987.8, 1480.0])]:
    for j, f in enumerate(notes):
        dd = t - a - j * 0.09
        tone = (dd >= 0) * (np.sin(2 * np.pi * f * dd) + 0.3 * np.sin(2 * np.pi * 2 * f * dd)) * np.exp(-dd * 3.0)
        out += 0.11 * np.stack([tone, tone], 1)

# 7) final fade 9.3-10 s
out *= np.clip((10.0 - t) / 0.7, 0, 1)[:, None]
out /= np.max(np.abs(out)) / 0.89

pcm = (out * 32767).astype(np.int16)
with wave.open(sys.argv[1] if len(sys.argv) > 1 else "intro.wav", "wb") as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR)
    wf.writeframes(pcm.tobytes())
print("audio ok")
