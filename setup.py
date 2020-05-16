'''
Build script for the Netsparker Rest API module
'''

from setuptools import setup
from codecs import open
from os import path
import netsparker_api

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="netsparker_api",
      packages=["netsparker_api"],
      version=netsparker_api.__version__,
      include_package_data=True,
      exclude_package_data={'': ['*.pyc']},
      author="Samy Younsi (Shino Corp')",
      author_email="samyyounsi@hotmail.fr",
      url="https://github.com/ShinoNoNuma/Netsparker-Rest-API",
      include_dirs=["."],
      license='MIT',
      description="An interface to Netsparker REST API",
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License"
      ],
      keywords="netsparker netsparker_api netsparker_rest netsparker_enterprise netsparker_team",
      install_requires=['requests >= 1.4'])