# image_word_extractor

### установка
[Установка tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html)

В каталоге проекта
```commandline
python -m pip install .
```


примеры находятся в examples

### структура
image_word_extractor - папка проекта

состоит из 3-х пакетов:
- api (сервер на fastapi)
- data_structures (структуры данных Image и Word)
- extractor (собственно код для выделения word в image)


### Docker
Сборка
```commandline
docker build
```
