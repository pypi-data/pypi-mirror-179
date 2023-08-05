import setuptools
import pyPhasesML

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyPhasesML",
    version=pyPhasesML.__version__,
    author="Franz Ehrlich",
    author_email="fehrlichd@gmail.com",
    description="A Framework for creating a boilerplate template for ai projects that are ready for MLOps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/tud.ibmt/pyPhases",
    packages=setuptools.find_packages(exclude="tests"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pyPhases"],
    python_requires=">=3.5",
)
