import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='Centre.PyCS',  
     version='0.1',
     author="BK",
     author_email="basknappers@gmail.com",
     description="Credits Blockchain Implementation in Python",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/akaitrade/Centre.PyCS",
     packages=setuptools.find_packages(include=['Connector', 'Connector.*']),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         'Programming Language :: Python :: 3',
     ],
 )