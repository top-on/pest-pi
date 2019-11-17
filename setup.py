import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pest_pi",
    version="0.1.0",
    author="Thorben Jensen",
    author_email="jensen.thorben@gmail.com",
    license="MIT",
    description=("Pest monitoring with Raspberry Pi."),
    long_description=read("README.md"),
    keywords="raspberry pi tensorflow",
    url="https://github.com/thorbenJensen/pest-pi",
    packages=["pest_pi"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "fastapi",
        "tensorflow~=1.13.0",
        "h5py",  # tensorflow
        "uvicorn",  # fastapi
        # picamera
        "pillow",  # tensorflow
        "wget",
    ],
    extras_require={
        "pi": ["picamera"],  # deployment on Raspberry Pi
        "dev": ["black", "pylama", "jupyter"],
    },
)
