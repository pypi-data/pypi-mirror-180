import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='choiceinput',
    version='0.1',
    scripts=['__init__.py', "choiceInput.py"],
    author="Patric Pintu",
    author_email="patric.personal99@gmail.com",
    description="choice input in terminal python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onlypatric/ChoiceInput",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
