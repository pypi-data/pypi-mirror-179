from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Exploratory Data Analysis'
LONG_DESCRIPTION = 'Python package to do exploratory data analysis and provide results in PDF'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="Exploratory-Data-Analysis", 
        version=VERSION,
        author="Abhilash Maspalli Srinivas",
        author_email="<abhilash_maspallisrinivas@comcast.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'EDA', 'PDF'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
)