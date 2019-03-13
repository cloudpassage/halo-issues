import os
import re
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    raw_init_file = read("haloissues/__init__.py")
    rx_compiled = re.compile(r"\s*__version__\s*=\s*\"(\S+)\"")
    ver = rx_compiled.search(raw_init_file).group(1)
    return ver


def get_long_description(fnames):
    retval = ""
    for fname in fnames:
        retval = retval + (read(fname)) + "\n\n"
    return retval


setup(
    name="haloissues",
    version=get_version(),
    author="CloudPassage",
    author_email="toolbox@cloudpassage.com",
    description="Multi-threaded issue retrieval",
    license="BSD",
    keywords="cloudpassage halo api issues",
    url="http://github.com/cloudpassage/halo-issues",
    packages=["haloissues"],
    install_requires=["cloudpassage >= 1.1.2",
                      "python-dateutil >= 2.6.0"],
    long_description=get_long_description(["README.rst"]),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security",
        "License :: OSI Approved :: BSD License"
        ],
    )
