import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covid-update", # Replace with your own username
    version="0.1.0",
    author="Tom Van Manen",
    author_email="tomvanmanen0@gmail.com",
    description="Print regional COVID case data from the BCCDC.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ciraben/covid-update",
    install_requires=["requests",],
    license='Hippocratic',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
