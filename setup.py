import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="linearalgebra-gp",
    version="0.0.1",
    author="Georges Petitpas",
    author_email="gpetitpas2@gmail.com",
    description="Linear Algebra functions for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gpetitpas/linearalgebra-gp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)