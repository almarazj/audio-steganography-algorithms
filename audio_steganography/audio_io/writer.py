import os
import soundfile as sf
from pydub import AudioSegment
import numpy as np


def audiosave(audio_data: np.ndarray, output_file: str, file_info: dict) -> None:
    """
    Save audio data to a file in various formats.
    """
    extension = file_info['ext']
    # Handle different formats
    if extension in ['.wav', '.flac']:
        # WAV and FLAC formats
        nbit = file_info['nbit']
        subtype = 'PCM_16' if nbit == 16 else 'PCM_24' if nbit == 24 else 'PCM_32'
        sf.write(output_file, audio_data, file_info['fs'], subtype=subtype)

    elif extension in ['.mp3', '.m4a', '.aac']:
        # Convert audio data to int16 if necessary
        if audio_data.dtype != np.int16:
            audio_data = (audio_data * 32767).astype(np.int16)

        # MP3, M4A, and AAC formats
        audio = AudioSegment(
            audio_data.tobytes(),
            frame_rate=file_info['fs'],
            sample_width=audio_data.dtype.itemsize,
            channels=1 if len(audio_data.shape) == 1 else audio_data.shape[1]
        )
        if extension == '.aac':
            print("Warning: Saving as .m4a instead of .aac!")
            extension = '.m4a'
            output_dir = os.path.dirname(output_file)
            output_file = os.path.join(output_dir, f"{file_info['name']}_dsss_encoded{extension}")
        audio.export(
            output_file,
            format=extension[1:],
            bitrate="128k"
        )

    elif extension in ['.ogg', '.oga']:
        # OGG and OGA formats
        audio = AudioSegment(
            audio_data.tobytes(),
            frame_rate=file_info['fs'],
            sample_width=audio_data.dtype.itemsize,
            channels=1 if len(audio_data.shape) == 1 else audio_data.shape[1]
        )
        audio.export(
            output_file,
            format="ogg",
            quality=file_info['nbit'] / 100.0
        )

    else:
        raise ValueError(f"Unsupported file format: {extension}")

    print(f"Audio saved to {output_file}")
