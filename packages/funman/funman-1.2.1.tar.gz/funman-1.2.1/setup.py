from pathlib import Path
from setuptools import setup, find_packages
import os

with open(os.path.join("src", "funman", '_version.py')) as version_file:
    version = version_file.readlines()[-1].split()[-1].strip("\"'")

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='funman',
      version=version,
      description='Functional Model Analysis Tool',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='',
      author='Dan Bryce',
      author_email='dbryce@sift.net',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'':'src'},
      install_requires=[
        "funman_dreal",
        "graphviz",
        "model2smtlib",
        "multiprocess",
        "tenacity"
        #"automates @ https://github.com/danbryce/automates/archive/e5fb635757aa57007615a75371f55dd4a24851e0.zip#sha1=f9b3c8a7d7fa28864952ccdd3293d02894614e3f"
      ],
      tests_require=["unittest"],
      zip_safe=False
      )