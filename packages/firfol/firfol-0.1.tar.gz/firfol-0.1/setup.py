from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='firfol',
     version='0.1',
     author="PSKPavanKalyan",
     author_email="poduripavankalyan@gmail.com",
     description="First and follow set finder in Compiler Construction",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/PSKPK/firfol",
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
