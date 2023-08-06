__author__ = "Eduardo Tuteggito Rosero"
__license__ = "GPL"
__version__ = "1.0.0-beta"
__maintainer__ = "Eduardo Tuteggito Rosero"
__email__ = "zerhiphop@live.com"
__status__ = "Development"
__date__ = "08/December/2022"

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    longDescription = fh.read()

setup(
    name="url_location",
    # namespace_packages=["url_location"],
    packages=find_packages(),
    version="1.0.0-beta",
    description="Package to retrieve the iso 3 short code of the country to which a URL belongs",
    long_description=longDescription,
    long_description_content_type="text/markdown",
    url="https://github.com/....",
    authors=[
        dict(name="Eduardo Tuteggito Rosero", email="zerhiphop@live.com")
    ],
    author="Eduardo Tuteggito Rosero",
    author_email="zerhiphop@live.com",
    license="MIT License",
    readme="README.md",
    install_requires=[""],
    keywords=["url", "country", "url_location"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
