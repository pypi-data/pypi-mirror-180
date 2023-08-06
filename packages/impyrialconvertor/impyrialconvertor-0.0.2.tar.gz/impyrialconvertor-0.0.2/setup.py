from setuptools import find_packages, setup

setup(
    author="Ebru Cucen",
    description="Converts units from different systems",
    name="impyrialconvertor",
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    install_requires=['numpy>=1.1'],
    python_requires='>=3.0',
    version="0.0.2",
)
