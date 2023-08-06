import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "shinigami",
    version = "0.0.4",
    author = "Hifumi1337",
    description = "Shinigami is an open source package allowing the user to generate and build a Dockerfile during runtime.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/stience/shinigami",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages = [
        "shinigami"
    ],
    python_requires = ">=3.6"
)