import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rede payments",
    version="1.0.1",
    author="Daniel H. G. Mescoloto",
    author_email="dan.gasperoni@gmail.com",
    description="A package to handle rede payments api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanDrix8391/erede-python",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
