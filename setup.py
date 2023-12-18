import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as file:
    requirements = file.read().splitlines()

PACKAGE_DIR = {"": "image_word_extractor"}
PACKAGES = setuptools.find_packages(include=["image_word_extractor", "image_word_extractor.*"])
setuptools.setup(
    name="image_word_extractor",
    version="0.0.2",
    author="Dunn Kopylov",
    author_email="38dunn@gmail.com",
    description="image word extractor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    package_dir=PACKAGE_DIR,
    packages=PACKAGES,

    python_requires=">=3.9"
)