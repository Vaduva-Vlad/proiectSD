import io
import socket
from process_audio import AudioProcessor

def get_spectrogram(audio_file):
    audio_processor = AudioProcessor(audio_file)
    return audio_processor.generate_spectrogram_image("spectrogram.png")

def main():
    host = '127.0.0.1'
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()

    connection, addr = s.accept()
    print("Successfully established connection with client")

    with open('output.mp3', 'wb') as f:
        while True:
            l = connection.recv(500)
            if not l:
                break
            f.write(l)
    print("File received")

    print("Sending spectrogram to client")
    image = get_spectrogram('output.mp3')
    connection.sendall(image)


    connection.close()
    s.close()

if __name__ == "__main__":
    main()