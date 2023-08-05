from setuptools import setup, find_packages

VERSION = '2.0.0' 
DESCRIPTION = 'Exploratory Data Analysis'
LONG_DESCRIPTION = 'Python package to do exploratory data analysis and provide results in PDF'

# Setting up
setup(
        name="exploratory", 
        version=VERSION,
        author="Abhilash",
        author_email="<abhilashmaspalli1996@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'EDA', 'PDF','Summary Statistics','Distribution Plot'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
)