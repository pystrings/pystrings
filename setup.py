from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="pystrings",
    version="0.0.34",
    author="Mahdi Gadget",
    author_email="mahdigadget20@gmail.com",
    description="A package For ease of working with strings",
    long_description=readme,
    long_description_content_type="text/markdown",
    URL = 'https://github.com/pystrings/pystrings',
    packages=find_packages(include=['pystrings']),
    python_requires = '>=3.6.0',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
