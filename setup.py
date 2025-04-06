from setuptools import setup, find_packages

setup(
    name="audio_steganography",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "librosa",
        "soundfile",
        "pydub"
    ],
)