from setuptools import setup


__project__ = "cin_term"
__version__ = "0.0.2"
__description__ = "cin_term is a terminal(only two to three commands) used for listing files and showing directory"
__packages__ = ["cin_term"]
__author__ = "Rigved Aneesh"
__author_email__ = "rigved.bob@gmail.com"
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
]
__keywords__ = ["cin_term", "terminal"]
__scripts__ = ["bin/cin_term"]
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


