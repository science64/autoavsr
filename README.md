<p align="center"><img width="160" src="doc/lip_white.png" alt="logo"></p>
<h1 align="center">Visual Speech Recognition for Multiple Languages</h1>

<div align="center">

[📘Introduction](#Introduction) |
[🛠️Preparation](#Preparation) |
[📊Benchmark](#Benchmark-evaluation) |
[🔮Inference](#Speech-prediction) |
[🐯Model zoo](#Model-Zoo) |
[📝License](#License)

</div>

## Authors

[Pingchuan Ma](https://mpc001.github.io/), [Alexandros Haliassos](https://dblp.org/pid/257/3052.html), [Adriana Fernandez-Lopez](https://scholar.google.com/citations?user=DiVeQHkAAAAJ), [Honglie Chen](https://scholar.google.com/citations?user=HPwdvwEAAAAJ), [Stavros Petridis](https://ibug.doc.ic.ac.uk/people/spetridis), [Maja Pantic](https://ibug.doc.ic.ac.uk/people/mpantic).

# AutoAVSR Pipelines

This package provides the pipeline modules from the AutoAVSR project. Easy to install via PIP

## Installation

```bash
pip install git+https://github.com/science64//autoavsr.git
```

## Usage

```python
from pipelines import AVSR, AVSRDataLoader, LandmarksDetector

# Initialize the models
avsr_model = AVSR()
data_loader = AVSRDataLoader()
detector = LandmarksDetector()


## Requirements
- Python >= 3.10
- PyTorch
- MediaPipe
- NumPy
```
