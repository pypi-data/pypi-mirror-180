import os
from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="tensorflow_image_models",
    version="0.0.11",
    author="DEEPOLOGY LAB",
    author_email="alaa.m.elmor@gmail.com",
    description="Tensorflow image models",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["tensorflow_image_models"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)