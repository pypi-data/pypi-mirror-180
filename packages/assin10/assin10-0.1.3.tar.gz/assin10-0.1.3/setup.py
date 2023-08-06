from setuptools import setup, find_packages

VERSION = '0.1.3' 
DESCRIPTION = 'The Assignment 10 - Emma Hall'
LONG_DESCRIPTION = 'This is my sumbission for the Assignment 10 in CS 501 Advanced Systems Programming.'

# Setting up
setup(
        name="assin10", 
        version=VERSION,
        author="Emma Hall",
        author_email="<elohall01@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'simpleCalpackage'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)