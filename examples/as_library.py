from image_word_extractor.data_structures import Image
from image_word_extractor.extractor import TesseractExtractor

import cv2
import os

np_img = cv2.imread(os.path.join("img", "exm.jpeg"))
im = Image(np_img)

word_extr = TesseractExtractor()
word_extr.set_extractor({"lang": "rus"})

words = word_extr.extract(im)
for w in words:
    print(w)
