from setuptools import setup


__project__ = "mil_term"
__version__ = "0.0.1"
__description__ = "mil_term is a terminal(only two to three commands) used for listing files and showing directory"
__packages__ = ["mil_term"]
__author__ = "Rigved Aneesh"
__author_email__ = "rigved.bob@gmail.com"
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
]
__keywords__ = ["mil_term", "terminal"]
__scripts__ = ["bin/mil_term"]
setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,
    author_email = __author_email__,
    classifiers = __classifiers__,
    keywords = __keywords__,
    scripts = __scripts__
)


