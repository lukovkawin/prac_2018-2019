import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkg",
    version="0.0.1",
    author="Danko && Kovaleva",
    author_email="ariolwork@gmail.com",
    description="hw2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
