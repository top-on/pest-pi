import os
from glob import glob
from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pest_pi",
    version="1.0.1",
    author="Thorben Jensen",
    author_email="jensen.thorben@gmail.com",
    license="MIT",
    description=("Pest monitoring with Raspberry Pi."),
    long_description=read("README.md"),
    keywords="raspberry pi tensorflow",
    url="https://github.com/thorbenJensen/pest-pi",
    packages=find_packages(),
    scripts=glob("bin/*"),
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
        "pillow",  # tensorflow
        "wget",
    ],
    extras_require={
        "pi": ["picamera"],  # deployment on Raspberry Pi
        "dev": ["black", "pylama", "jupyter"],
    },
)
