from setuptools import setup, find_namespace_packages
from importlib import import_module

with open("requirements.txt", 'r') as f:
    require = f.read().splitlines()

with open("README.md", 'r') as f:
    long_description = f.read()

version = import_module("visionaire4.version").__version__

extras_require = {
    "dev": [
        "pytest",
        "pytest-cov",
        "flake8",
        "twine",
        "wheel"
    ]
}

setup(
    name="visionaire4",
    version=version,
    description="Visionaire4 maintenance tools suite",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://pypi.org/project/visionaire4/",
    author="Tri Wahyu Utomo",
    author_email="tri@nodeflux.io",
    packages=find_namespace_packages(),
    entry_points={
        "console_scripts": ["visionaire4 = visionaire4.__main__:main"]
    },
    python_requires=">=3.6",
    install_requires=require,
    extras_require=extras_require
)
