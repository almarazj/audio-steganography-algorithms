import numpy as np


def dsss_decoder(signal: np.ndarray, length_msg: int, length_min: int = 8*1024) -> str:
    """
    Decodes a DSSS encoded signal back into a text message.
    """
    # Initialize the decoded message
    decoded_message = []
    
    L2 = np.floor(len(signal)/length_msg)
    segment = max(length_min, L2)
    
    # Iterate over the signal in chunks of length_min
    for i in range(0, len(signal), segment):
        # Extract the chunk
        chunk = signal[i:i + segment]
        
        # Calculate the average value of the chunk
        avg_value = np.mean(chunk)
        
        # Determine if the bit is 1 or 0 based on the average value
        if avg_value > 0:
            decoded_message.append('1')
        else:
            decoded_message.append('0')
    
    # Convert binary string to characters
    binary_string = ''.join(decoded_message)
    chars = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    
    # Convert binary to text
    text = ''.join(chr(int(char, 2)) for char in chars if len(char) == 8)
    
    return text
