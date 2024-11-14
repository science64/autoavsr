# Import the classes to make them available at package level
from .model import AVSR
from .data.data_module import AVSRDataLoader
from .detectors.mediapipe.detector import LandmarksDetector

__version__ = "0.2.1"

# Make these classes available at package level
__all__ = ['AVSR', 'AVSRDataLoader', 'LandmarksDetector']