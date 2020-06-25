import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='uchkin_diploma',  
    version='1.0.3',
    author="Dmytro Uchkin",
    author_email="dimon97xl@gmail.com",
    description="Neural Network for digit recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DemjanUA/uchkin_diploma",
    packages=[
        'uchkin_diploma'
    ],
    install_requires=[
        'scipy',
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)