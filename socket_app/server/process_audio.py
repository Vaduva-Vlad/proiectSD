from io import BytesIO

import librosa
import matplotlib.pyplot as plt
import numpy as np



class AudioProcessor:
    def __init__(self, filename):
        self.filename = filename

    def generate_spectrogram_image(self, output_path):
        y, sr = librosa.load(self.filename)
        spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
        fig, ax = plt.subplots()
        spectrogram_dB = librosa.power_to_db(spectrogram, ref=np.max)
        img = librosa.display.specshow(spectrogram_dB, x_axis='time', y_axis='mel', sr=sr, fmax=8000, ax=ax)
        fig.colorbar(img, ax=ax, format='%+2.0f dB')
        ax.set(title='Spectrogram')
        buffer=BytesIO()
        plt.savefig(buffer,format='png')
        return buffer.getvalue()


if __name__ == "__main__":
    audio_processor = AudioProcessor("output.mp3")
    spectrogram = audio_processor.generate_spectrogram_image("spectrogram.png")
    print(spectrogram)