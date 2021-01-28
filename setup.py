from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="pystrings",
    version="0.0.32",
    author="Mahdi Gadget",
    author_email="mahdigadget20@gmail.com",
    description="A package For ease of working with strings",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/pystrings",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
