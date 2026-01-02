from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(requirements_file: str) -> List[str]:
    """Reads the requirements file and returns a list of dependencies."""
    with open(requirements_file, "r") as file:
        requirements = file.readlines()
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return [req.strip() for req in requirements if req.strip()]

setup(
    name="my_package",
    version="0.1.0",
    author="Rohan Sharma",
    author_email="rohan.sharma1234987650@gmail.com",
    description="A brief description of my package",
    packages=find_packages(),
    install_requires=get_requirements(requirements_file="requirements.txt"),
)