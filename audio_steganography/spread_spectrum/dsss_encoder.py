import numpy as np


def dsss_encoder(signal: np.ndarray, text: str, min_length: int = 10*1024) -> np.ndarray:
    
    """
    Encodes a text message into a signal using Direct Sequence Spread Spectrum (DSSS) encoding.
    """
    # Convert text to binary
    binary_message = ''.join(format(ord(char), '08b') for char in text)
    print(f"Length of the signal: {len(signal)}")
    print(f"Shape of signal: {signal.shape}")
    print(f"Length of the message: {len(binary_message)}")
    L2 = int(np.floor(signal.shape[1]/len(binary_message)))
    segment = max(min_length, L2)
    
    # Ensure the signal can be divided into segments
    total_length = int(np.floor(segment * len(binary_message)))
    print(f"Total length of the signal: {total_length}")
    
    if total_length > signal.shape[1]:
        raise ValueError("Signal is too short to encode the entire message with the given segment size.")

    # Generate spreading code
    spreading_code = np.random.choice([-1, 1], size=(total_length,))
    spreading_code = spreading_code * 0.1  # Scale down the spreading code
    # Encode the message
    encoded_signal = np.zeros(signal.shape[1])
    
    for i, bit in enumerate(binary_message):
        start = i * segment
        end = (i + 1) * segment
        if bit == '1':
            encoded_signal[start:end] = signal[0][start:end] + signal[0][start:end] * spreading_code[start:end]
        else:
            encoded_signal[start:end] = signal[0][start:end] + signal[0][start:end] * -spreading_code[start:end]
    
    noise = encoded_signal - signal[0]
    snr = 10 * np.log10(np.sum(signal[0]**2) / np.sum(noise**2))
    print(f"SNR: {snr} dB")
    
    return encoded_signal