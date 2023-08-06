from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="biquaternions",
    version="0.0.2",
    author="MiLis",
    author_email="quaternionlab@gmail.com",
    description="A package for works with biquaternions",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/QuaternionLab/biquaternions/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)