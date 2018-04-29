""" Library to construct particle based systems for simulation.
"""

import os
from setuptools import setup, find_packages


try:
    import numpy
except ImportError:
    print('-'*80, file=sys.stderr)
    print("""Error: building mdtraj requires numpy""", file=sys.stderr)
    print('-'*80, file=sys.stderr)
    sys.exit(1)


CLASSIFIERS = """\
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Scientific/Engineering :: Bio-Informatics
Topic :: Scientific/Engineering :: Chemistry
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='sysbead',
      version="2018a1",
      author='Hector Martinez-Seara',
      author_email='hseara@gmail.com',
      description=("Library to construct particle based systems for simulation."),
      long_description=read('README.md'),
      license='LGPLv3.0+',
      url='http://sysbead.com',
      download_url = "https://github.com/hseara/sysbead/",
      platforms=['Linux', 'Mac OS-X'],
      packages=find_packages(),
      classifiers=CLASSIFIERS.splitlines(),
)
