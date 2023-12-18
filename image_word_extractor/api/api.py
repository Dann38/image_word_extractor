import base64
import numpy as np
import cv2

from fastapi import FastAPI

import uvicorn
from . import schemas
from typing import List

from image_word_extractor.data_structures import Image
from image_word_extractor.extractor import TesseractExtractor

app = FastAPI()
word_extr = TesseractExtractor()
word_extr.set_extractor({"lang": "rus"})


def read_base64(base64_img: str):
    np_arr = np.fromstring(base64.b64decode(base64_img), np.uint8)
    cv2_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return Image(cv2_img)


def run_api(host: str, port: int) -> None:
    uvicorn.run(app=app, host=host, port=port)


@app.post("/word_extract/", response_model=schemas.Document)
async def read_images(img_doc: schemas.Document):
    img = read_base64(img_doc.base64)

    words_list = word_extr.extract(img)
    img_doc.word_list = [word.get_point_and_size() for word in words_list]
    img_doc.text_list = [word.text for word in words_list]
    return img_doc
