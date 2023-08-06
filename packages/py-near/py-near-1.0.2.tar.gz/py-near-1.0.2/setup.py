from setuptools import setup
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files("pynear")

setup(
    name="py-near",
    author_email="petr@herewallet.app",
    url="https://github.com/pvolnov/py-near",
    packages=["pynear"],
    python_requires=">=3.6",
    package_data={"": extra_files},
    project_urls={
        "Documentation": "https://py-near.readthedocs.io/en/latest",
        "Funding": "https://opencollective.com/py-near",
        "Twitter": "https://twitter.com/p_volnov",
        "Source": "https://github.com/pvolnov/py-near",
        "Tracker": "https://github.com/pvolnov/py-near/issues",
    },
    version="1.0.2",
    description="Pretty simple and fully asynchronous framework for working with NEAR blockchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Petr Volnov",
    license="MIT",
    install_requires=["base58", "ed25519", "aiohttp"],
)
