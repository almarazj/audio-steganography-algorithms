from audio_steganography.spread_spectrum.data_embedding import data_embedding


filepath = "/home/jalma/repos/audio-steganography-algorithms/audio_files/test_file.mp3"
msg = "Hello, this is a test message for DSSS encoding."

data_embedding(filepath, msg)
