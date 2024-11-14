from setuptools import setup, find_packages

# Core dependencies needed for the functionality
CORE_DEPENDENCIES = [
    'numpy>=1.26.4',
    'torch>=2.1.0',  # Adjusted for Python 3.12 compatibility
    'torchaudio>=2.1.0',
    'torchvision>=0.16.0',
    'mediapipe>=0.10.18',
    'opencv-python>=4.8.0',
    'opencv-contrib-python>=4.8.0',
    'scipy>=1.11.3',
    'scikit-image>=0.22.0',
    'matplotlib>=3.8.0',
    'av>=13.1.0',
    'ffmpeg-python>=0.2.0',
    'sounddevice>=0.5.1',
]

setup(
    name="autoavsr-pipelines",
    version="0.1.0",
    packages=find_packages(include=['pipelines', 'pipelines.*']),
    python_requires=">=3.10",  # Specify Python 3.12
    install_requires=CORE_DEPENDENCIES,
    description="Pipeline modules for AutoAVSR",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/science64/autoavsr",
)