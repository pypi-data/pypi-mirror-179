from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name="unscramble_dc",
    version="0.0.1",
    author="Brahmani Nutakki",
    description="Finds words from scrambled letters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["unscramble"],
    package_dir={'unscramble': 'unscramble'},
    install_requires=['nltk']
)
