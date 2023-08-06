import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read() + open("CHANGELOG.txt").read()

setuptools.setup(

    name="Image To ASCII generator", # Replace with your username

    version="1.0.0",

    author="Omar Maaoune",

    author_email="Electromaster20000@gmail.com",

    description="Image to ASCII converter",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/electromaster0395/image-to-ascii-converter-library",

    license = "MIT",

    keywords = "converter",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)