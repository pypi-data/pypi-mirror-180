"""MyrtDesk setup script"""
import setuptools

with open(".version", "r", encoding="utf-8") as fh:
    version = fh.read()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiodatagram",
    version=version,
    author="Mikhael Khrustik",
    description="A set of utilities to handle UDP in the asyncio context",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        'aiodatagram',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
    package_dir={'':'.'},
)
