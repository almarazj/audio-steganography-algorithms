import os
from audio_steganography.audio_io.writer import audiosave
from audio_steganography.audio_io.reader import audioload
from audio_steganography.spread_spectrum.dsss_encoder import dsss_encoder


def data_embedding(filepath: str, msg: str) -> None:
    """
    Embed a message into audio data using spread spectrum steganography.
    """
    # Load the audio file
    file_info = audioload(filepath)
     
    # Embed the message using spread spectrum steganography
    encoded_data = dsss_encoder(file_info['data'], msg)
    
    output_dir = os.path.dirname(filepath)
    output_file = os.path.join(output_dir, f"{file_info['name']}_dsss_encoded{file_info['ext']}")

    # Save the stego audio data to a file
    audiosave(encoded_data, output_file, file_info)