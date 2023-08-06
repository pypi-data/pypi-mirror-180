import os

import setuptools

# get the dependencies #
# Get the current directory path
lib_folder = os.path.dirname(os.path.realpath(__file__))
# get the "requirements.txt" file path
requirement_path = os.path.join(lib_folder, "requirements.txt")
# to store the required packages
install_requires = []
# now open the file and stored the required packages' names
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setuptools.setup(
    name = "imathlogic",
    version = "0.0.6",
    author = "Sayan Roy",
    author_email = "rsayan553@gmail.com",
    url = "https://github.com/Sayan-Roy-729/iMathLogic",
    packages = ["imathlogic", "imathlogic.supervised"],
    description = "Get the result of all types of algorithms in a simple way",
    license = "MIT",
    install_requires = install_requires
)
