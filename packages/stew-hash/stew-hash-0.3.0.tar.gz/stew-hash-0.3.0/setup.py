import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="stew-hash",
    version="0.3.0",
    author="apinanyogaratnam",
    author_email="apinanapinan@icloud.com",
    description="A simple hashing library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apinanyogaratnam/stew-hash",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10.4",
    install_requires=[],
)
