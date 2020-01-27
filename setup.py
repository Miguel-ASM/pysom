import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pySOM-Miguel-ASM", # Replace with your own username
    version="0.0.1",
    author="Miguel Angel Simon Martinez",
    author_email="miguel.a.s.martinez@gmail.com",
    description="split operator method in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Miguel-ASM/pysom",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
