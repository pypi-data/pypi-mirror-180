from setuptools import setup, find_packages

VERSION = '0.0.5' 
DESCRIPTION = 'Twitter Sentiment Analysis package'
LONG_DESCRIPTION = 'Thank you for downloading the file '

# Setting up
setup(
        name="analyze_the_shit_out_of_me", 
        version=VERSION,
        author="Mirzabek Matyakubov",
        author_email="<markmatyakubov@gmail.com",
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