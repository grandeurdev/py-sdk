# Import the setup package
import io
import os

import setuptools

# Package metadata.
name = 'grandeurcloud'
description = 'This SDK has been designed to enable developers integrate Grandeur Cloud into SOCs with Python'
version = '0.1.1'

# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 3 - Alpha"

dependencies = [
    'websocket-client',
	'pyee',
]

# Root directory
package_root = os.path.abspath(os.path.dirname(__file__))

# Readme file
readme_filename = os.path.join(package_root, "README.md")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

# Only include packages under the 'grandeurcloud' namespace.
packages = [
    package
    for package in setuptools.PEP420PackageFinder.find()
    if package.startswith("grandeurcloud")
]

# Determine which namespaces are needed.
namespaces = ["grandeurcloud"]
if "grandeurcloud.apollo" in packages:
    namespaces.append("grandeurcloud.apollo")

setuptools.setup(
    name = name,
    version = version,
    description = description,
    long_description = readme,
    author = 'Grandeur Technologies',
  	author_email = 'hi@grandeur.tech',
    license = 'MIT',
    url = "https://github.com/grandeurtech/grandeurcloud-py-sdk",
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