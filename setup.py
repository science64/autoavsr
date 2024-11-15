from setuptools import setup, find_packages

# Core dependencies including espnet
CORE_DEPENDENCIES = [
    'numpy==1.26.4',  # Match espnet requirement
    'torch>=2.1.0',
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
    # 'espnet>=202401',
    # 'espnet-model-zoo>=0.1.7',
    # 'espnet-tts-frontend>=0.0.3',
    'sentencepiece>=0.1.97',
    'hydra-core>=1.3.2',
    'omegaconf>=2.3.0',
]

setup(
    name="autoavsr_pipelines",  # Changed package name to match import
    version="0.2.1",
    packages=['autoavsr_pipelines'],  # Specify the package explicitly
    package_dir={'autoavsr_pipelines': 'pipelines'},  # Map the directory to the package name
    python_requires=">=3.10",
    install_requires=CORE_DEPENDENCIES,
    description="AutoAVSR Pipelines Package",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/science64/autoavsr",
    include_package_data=True,
    package_data={
        'autoavsr_pipelines': [
            'configs/**/*',
            'espnet/**/*',
            'hydra_configs/**/*',
            '**/*',
        ],
    },
)