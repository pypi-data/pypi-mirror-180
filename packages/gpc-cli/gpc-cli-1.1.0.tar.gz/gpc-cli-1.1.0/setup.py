from setuptools import setup, find_packages
from io import open
from os import path
import pathlib


# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()

# automatically captured required modules for install_requires in requirements.txt and as well as configure
# dependency links

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()


setup(
    name="gpc-cli",
    description="CLI utility for detecting weak spots in GitHub profiles",
    version="1.1.0",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "gpc=src:cli"
        ]
    },
    author="Roland Fridemanis",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/rolandsfr/github-profile-checker",
     author_email="rolands.affaires@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)
