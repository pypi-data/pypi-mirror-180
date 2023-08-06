from setuptools import setup, find_packages
import codecs


VERSION = '1.8.13'
DESCRIPTION = 'Streaming bytes data via networks'
LONG_DESCRIPTION = 'A package that allows to build simple streams of bytes data.'

# Setting up
setup(
    name="VerifySteream",
    version=VERSION,
    author="neon",
    author_email="neon@webmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)