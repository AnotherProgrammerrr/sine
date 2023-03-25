import numpy as np
import sounddevice as sd
from matplotlib import pyplot as plt
from PIL import Image, ImageOps

def generate_sound_and_graph(duration, freq, amp=.4, sample_rate=44100):
    plt.clf()

    num_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    window = np.hamming(num_samples)
    y = amp * np.sin(2 * np.pi * freq * t) * window

    pause_duration = 0.200
    num_pause_samples = int(sample_rate * pause_duration)
    y = np.concatenate([y, np.zeros(num_pause_samples)])

    sd.play(y, sample_rate)
    sd.wait()

    duration = .01
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, num_samples, endpoint=False)

    plt.grid(True)

    amp = 1
    y = amp * np.sin(2*np.pi*freq*t)
    plt.ylim(-2, 2)

    plt.plot(t, y, color='#00fe92')
    plt.title(f"Gerador de senoides")

    plt.xlabel('Tempo  ')
    plt.ylabel('Amplitude')

    plt.savefig('files/tempfile.png')

    img = Image.open('files/tempfile.png')
    img = img.convert('RGB')
    img = ImageOps.invert(img)
    img.save('files/tempfile.png')
    

generate_sound_and_graph(.5, 327)
generate_sound_and_graph(.5, 413)
generate_sound_and_graph(.5, 0)