import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='uchkin_diploma',  
    version='0.1',
    scripts=['uchkin_diploma'] ,
    author="Dmytro Uchkin",
    author_email="dimon97xl@gmail.com",
    description="Neural Network for digit recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DemjanUA/uchkin_diploma",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)