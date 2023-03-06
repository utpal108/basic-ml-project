from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    # return the list of required package list
    f = open(file_path, 'r')
    requirements = [req.replace("\n", "") for req in f.readlines()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="Basic ML Project",
    version="0.0.1",
    author="Utpal Paul",
    author_email="utpalpaul108@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
