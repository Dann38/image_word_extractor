from abc import ABC, abstractmethod
from image_word_extractor.data_structures import Image, Word
from typing import List, Dict


class BaseExtractor(ABC):
    def __init__(self):
        self.conf = None

    def set_extractor(self, conf: Dict):
        self.conf = conf

    @abstractmethod
    def extract(self, img: Image) -> List[Word]:
        pass
