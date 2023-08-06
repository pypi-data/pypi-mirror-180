import setuptools
from pathlib import Path


def get_version() -> str:
    """returns current version of the project

    :return: Current version of the project
    :rtype: str
    """
    version_filename = Path(__file__).parent / "metaibricks/_version.py"
    with open(version_filename, "r") as fp:
        version_line = fp.readlines()[0]
    return version_line.split()[-1].strip('"')


with open("README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="metaibricks",
    version=get_version(),
    author="LabIA-MF",
    author_email="lab_ia@meteo.fr",
    description="Met-AI-Bricks : Meteorological AI Bricks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab.meteo.fr/deep_learning/ai-lab-tools/met-ai-bricks",
    packages=setuptools.find_packages(),
    install_requires=[
        "pydantic",
        "requests",
        "beautifulsoup4",
        "mflog",
    ],
)
