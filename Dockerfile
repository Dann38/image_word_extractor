ARG REPOSITORY="docker.io"
FROM ubuntu:22.04

WORKDIR /image_word_extractor


# install python3
RUN apt-get update && apt-get install -y python3 python3-pip software-properties-common ffmpeg libsm6 libxext6

# install tesseract
RUN add-apt-repository -y  ppa:alex-p/tesseract-ocr-devel && apt update --allow-releaseinfo-change && apt install -y tesseract-ocr tesseract-ocr-rus

#
COPY ./setup.py /image_word_extractor/setup.py
COPY ./requirements.txt /image_word_extractor/requirements.txt
COPY ./image_word_extractor /image_word_extractor/image_word_extractor
COPY ./README.md /image_word_extractor/README.md

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install /image_word_extractor/.