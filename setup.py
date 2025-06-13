from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description - f.read()

with open("requeriments.txt") as f:
    requeriments = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Genilson Junior"
    description="Processamento de cores nas imagens"
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gejunior/processando-imagens-em-python.git"
)