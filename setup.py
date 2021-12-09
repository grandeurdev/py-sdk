# Import the setup package
from os import path
import io

import setuptools

# Package metadata.
name = 'grandeur'
description = 'This SDK has been designed to enable developers integrate Grandeur into SOCs with Python'
version = '0.1.6'

# Setup long description
directory = path.abspath(path.dirname(__file__))
with io.open(path.join(directory, 'README.md'), encoding="utf-8") as f:
    long_description = f.read()

# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 3 - Alpha"

dependencies = [
    'websocket-client',
	'pyee',
]

# Only include packages under the 'grandeur' namespace.
packages = [
    package
    for package in setuptools.PEP420PackageFinder.find()
    if package.startswith("grandeur")
]

# Determine which namespaces are needed.
namespaces = ["grandeur"]
# if "grandeurcloud.apollo" in packages:
#     namespaces.append("grandeurcloud.apollo")

setuptools.setup(
    name = name,
    version = version,
    description = description,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = 'Grandeur Technologies',
  	author_email = 'hi@grandeur.tech',
    license = 'MIT',
    url = "https://github.com/grandeurtech/py-sdk",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms = "Posix; MacOS X; Windows",
    packages = packages,
    namespace_packages = namespaces,
    install_requires = dependencies,
    python_requires = ">=3.6",
    include_package_data = True,
    zip_safe = False,
)