from setuptools import setup, find_namespace_packages
from codecs import open
from os import path

__version__ = '0.1.0'

here = path.abspath(path.dirname(__file__))

# Get the requirements; ignore commented lines
with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xicam.SymmetryPlugin',
    version=__version__,
    description='',
    long_description=long_description,
    url='',
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='Xi-cam',
    packages=find_namespace_packages(exclude=['docs', 'tests*']),
    install_requires=requirements,
    include_package_data=True,
    author='Alexander Hexemer',
    author_email='ahexemer@lbl.gov',
    entry_points={
        'xicam.plugins.GUIPlugin':
            ['symmetry_plugin = xicam.symmetryplugin:SymmetryPlugin'],
        'xicam.plugins.OperationPlugin':
            [
            ]
    }
)
