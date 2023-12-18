from abc import ABC

import numpy as np


class Image(ABC):
    def __init__(self, image: np.ndarray):
        self.image = image

