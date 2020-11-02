# Import the setup package
from distutils.core import setup

# Setup details of the package
setup(
  name = 'grandeurcloud',
  packages = ['grandeurcloud'],
  version = '0.1', 
  license='MIT',
  description = 'This SDK has been designed to enable developers integrate Grandeur Cloud into SOCs with Python',
  author = 'Grandeur Technologies',
  author_email = 'hi@grandeur.tech',
  url = 'https://github.com/grandeurtech/grandeurcloud-py-sdk',
  download_url = 'https://github.com/grandeurtech/grandeurcloud-js-sdk/archive/master.tar.gz',
  keywords = ['IoT', 'Grandeur Technologies', 'Grandeur Cloud'],
  install_requires=[
          'websocket-client',
          'pyee',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)