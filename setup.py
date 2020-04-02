import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-kzt-exchangerates",
    version="0.1.2",
    author="Dastan Abdrakhmanov",
    author_email="dastand.climber@gmail.com",
    description=("Python library to get exchange rates from Kazakhstan's "
                 "National Bank"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dclimber/python-kzt-exchangerates",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
