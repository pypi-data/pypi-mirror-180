import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="HashToDocx", 
    version="1.0.0",
    author="Qerogram",
    author_email="qerogram@google.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qerogram/HashToDocument",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)