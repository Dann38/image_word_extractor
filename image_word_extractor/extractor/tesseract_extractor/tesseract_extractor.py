from typing import List

from ..base_extractor import BaseExtractor
from image_word_extractor.data_structures import Image, Word


import pytesseract


class TesseractExtractor(BaseExtractor):
    def extract(self, img: Image) -> List[Word]:
        tesseract_bboxes = pytesseract.image_to_data(
            config=self._get_conf_tesseract(),
            image=img.image,
            output_type=pytesseract.Output.DICT)
        word_list = []
        for index_bbox, level in enumerate(tesseract_bboxes["level"]):
            if level == 5:
                word = Word()
                word.set_point_and_size({
                    "x0": tesseract_bboxes["left"][index_bbox],
                    "y0": tesseract_bboxes["top"][index_bbox],
                    "w": tesseract_bboxes["width"][index_bbox],
                    "h": tesseract_bboxes["height"][index_bbox],
                })
                word.set_text(tesseract_bboxes["text"][index_bbox])

                word_list.append(word)
        return word_list

    def _get_conf_tesseract(self):
        conf_str = ""
        if "lang" in self.conf.keys():
            conf_str += f"-l {self.conf['lang']}"
        return conf_str
