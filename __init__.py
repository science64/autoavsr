from pipelines.model import AVSR
from pipelines.data.data_module import AVSRDataLoader
from pipelines.detectors.mediapipe.detector import LandmarksDetector

__version__ = "0.2.0"

# Make these classes available at package level
__all__ = ['AVSR', 'AVSRDataLoader', 'LandmarksDetector']