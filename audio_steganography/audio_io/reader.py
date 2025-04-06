import os
import librosa
import soundfile as sf


def audioload(filepath):
    """
    Load audio file and extract important information.
    Supports .wav, .flac, .mp3, .m4a, .aac, .ogg, .oga formats.

    Parameters:
        filepath (str): Path to the audio file.

    Returns:
        dict: A dictionary containing audio data, sample rate, and metadata.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    file_ext = os.path.splitext(filepath)[1].lower()
    supported_formats = ['.wav', '.flac', '.mp3', '.m4a', '.aac', '.ogg', '.oga']

    if file_ext not in supported_formats:
        raise ValueError(f"Unsupported file format: {file_ext}")

    audio_info = {}
    audio_info['path'] = filepath
    audio_info['name'] = os.path.splitext(os.path.basename(filepath))[0]
    audio_info['ext'] = file_ext

    try:
        if file_ext in ['.wav', '.flac', '.ogg', '.oga']:
            data, sr = sf.read(filepath)
            audio_info['data'] = data
            audio_info['fs'] = sr
            audio_info['nbit'] = sf.info(filepath).subtype_info
        elif file_ext in ['.mp3', '.m4a', '.aac']:
            data, sr = librosa.load(filepath, sr=None, mono=False)
            audio_info['data'] = data
            audio_info['fs'] = sr
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")

        audio_info['len'] = len(audio_info['data'])
        audio_info['ch'] = 1 if len(audio_info['data'].shape) == 1 else audio_info['data'].shape[0]
    except Exception as e:
        raise RuntimeError(f"Error reading audio file: {e}")

    return audio_info
