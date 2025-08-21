from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    req = []
    with open(file_path) as f:
        req = [line.strip() for line in f]
        req = [r for r in req if r and not r.startswith("#")]
        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    return req

setup(
    name="mlproject",
    version="0.0.1",
    author="Anmol",
    author_email="anmol752005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
