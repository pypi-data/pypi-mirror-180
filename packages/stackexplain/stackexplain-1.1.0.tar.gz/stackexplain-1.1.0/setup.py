try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open
import sys

if sys.version_info[:3] < (3, 0, 0):
    print("Requires Python 3 to run.")
    sys.exit(1)

with open("README.md", encoding="utf-8") as file:
    readme = file.read()

setup(
    name="stackexplain",
    version="1.1.0",
    description="Command-line tool that automatically explains your error message using ChatGPT",
    #long_description=readme,
    #long_description_content_type="text/markdown",
    url="https://github.com/shobrook/stackexplain",
    author="shobrook",
    author_email="shobrookj@gmail.com",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Software Development :: Debuggers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    keywords="chatgpt cli commandline error message stack trace stackexplain explanation",
    include_package_data=True,
    packages=["stackexplain"],
    entry_points={"console_scripts": ["stackexplain = stackexplain.stackexplain:main"]},
    install_requires=["revChatGPT", "pygments"],
    requires=["revChatGPT", "pygments"],
    python_requires=">=3",
    license="MIT"
)
