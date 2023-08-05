from setuptools import setup

VERSION = '1.0.0'
DESCRIPTION = 'Checking if a number is a power of 2'
LONG_DESCRIPTION = 'Package to check if a given number is a power of 2.'

# Setting up
setup(
    name="isPowerOfTwo",
    version=VERSION,
    author="Omkar Ingale",
    author_email="<omkar001@duck.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    install_requires=[],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)