from setuptools import setup, find_packages

VERSION = '0.0.7' 
DESCRIPTION = 'CS501 Assignment 10 RA'
LONG_DESCRIPTION = 'Assignment 10 for CS501 done by Ryan August'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="CS501A10Assignment", 
        version=VERSION,
        author="Ryan August",
        author_email="<raugust@g.emporia.edu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)