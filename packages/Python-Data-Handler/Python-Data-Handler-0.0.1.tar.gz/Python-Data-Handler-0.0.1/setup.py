import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Python-Data-Handler",
    version="0.0.1",
    author="Shikiso",
    author_email="author@example.com",
    description="This repository is a Python built data handler that uses JSON, SQL, SQLite3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shikiso/Python-Data-Handler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)